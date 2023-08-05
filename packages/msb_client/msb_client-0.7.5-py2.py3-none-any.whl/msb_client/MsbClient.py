# -*- coding: utf-8 -*-
"""
Copyright (c) 2017
Fraunhofer Institute for Manufacturing Engineering
and Automation (IPA)
Author: Daniel Stock
mailto: daniel DOT stock AT ipa DOT fraunhofer DOT com
See the file "LICENSE" for the full license governing this code.
"""

import websocket, threading, json, jsonschema, jsonpickle, ssl, time, uuid, os, logging
from random import randint
import datetime

from .Event import Event
from .ComplexDataFormat import ComplexDataFormat
from .Function import Function
from .DataFormat import getDataType


class MsbClient(websocket.WebSocketApp):
    def __init__(
        self, service_type=None, uuid=None, name=None, description=None, token=None
    ):
        self.connected = False
        self.registered = False
        self.autoReconnect = True
        self.reconnecting = False
        self.userDisconnect = False
        self.reconnectInterval = 10
        self.keepAlive = False
        self.heartbeat_interval = 8
        self.sockJsFraming = True

        self.debug = False
        self.trace = False
        self.dataFormatValidation = True

        self.eventCache = []
        self.eventCacheEnabled = True
        self.eventCacheSize = 1000
        self.maxMessageSize = 100000000

        self.functions = {}
        self.events = {}
        self.configuration = {}
        self.configuration["parameters"] = {}
        self.msb_url = ""
        self._msb_url = ""

        self.ws = None
        self.hostnameVerification = False
        self.threadAsDaemonEnabled = False

        if (service_type or uuid or name or description or token) is not None:
            self.service_type = service_type
            self.uuid = uuid
            self.name = name
            self.description = description
            self.token = token
        else:
            self.readConfig()

    jsonpickle.set_encoder_options("json", sort_keys=False, indent=4)
    jsonpickle.set_preferred_backend("json")

    MSBMessageTypes = [
        "IO",
        "NIO",
        "IO_CONNECTED",
        "IO_REGISTERED",
        "IO_PUBLISHED",
        "NIO_ALREADY_CONNECTED",
        "NIO_REGISTRATION_ERROR",
        "NIO_UNEXPECTED_REGISTRATION_ERROR",
        "NIO_UNAUTHORIZED_CONNECTION",
        "NIO_EVENT_FORWARDING_ERROR",
        "NIO_UNEXPECTED_EVENT_FORWARDING_ERROR",
    ]

    def disableSockJsFraming(self, sockJsFraming):
        self.sockJsFraming = not sockJsFraming
        self.keepAlive = sockJsFraming

    def disableEventCache(self, disableEventCache):
        self.eventCacheEnabled = not disableEventCache

    def enableDataFormatValidation(self, dataFormatValidation):
        self.dataFormatValidation = dataFormatValidation

    def sendBuf(self):
        for idx, msg in enumerate(self.eventCache):
            try:
                if self.connected and self.registered:
                    logging.debug("SENDING (BUF): " + msg)
                    if self.sockJsFraming:
                        _msg = self.objectToJson(msg).replace("\\n", "")
                        self.ws.send('["E ' + _msg[1:-1] + '"]')
                    else:
                        self.ws.send("E " + msg)
                    self.eventCache.pop(idx)
            except Exception:
                pass

    def on_message(self, message):
        if self.sockJsFraming:
            if self.debug and message.startswith("h"):
                logging.debug("♥")
            message = message[3:-2]
        if message in self.MSBMessageTypes:
            logging.info(message)
            if message == "IO_CONNECTED":
                if self.reconnecting:
                    self.reconnecting = False
                    if self.sockJsFraming:
                        _selfd = json.dumps(
                            self.objectToJson(self.getSelfDescription())
                        ).replace("\\n", "")
                        self.ws.send('["R ' + _selfd[1:-1] + '"]')
                    else:
                        self.ws.send(
                            "R " + self.objectToJson(self.getSelfDescription())
                        )
            if message == "IO_REGISTERED":
                self.registered = True
                if self.eventCacheEnabled:
                    self.connected = True
                    self.sendBuf()
            elif message == "NIO_ALREADY_CONNECTED":
                if self.connected:
                    try:
                        self.ws.close()
                    except Exception:
                        pass
            elif message == "NIO_UNEXPECTED_REGISTRATION_ERROR":
                if self.connected:
                    try:
                        self.ws.close()
                    except Exception:
                        pass
            elif message == "NIO_UNAUTHORIZED_CONNECTION":
                if self.connected:
                    try:
                        self.ws.close()
                    except Exception:
                        pass
        if message.startswith("C"):
            jmsg = message.replace('\\"', '"')
            jmsg = json.loads(jmsg[2:])
            logging.info(str(jmsg))
            if jmsg["functionId"] not in self.functions:
                if jmsg["functionId"].startswith("/") and not jmsg[
                    "functionId"
                ].startswith("//"):
                    jmsg["functionId"] = jmsg["functionId"][1:]
            if jmsg["functionId"] in self.functions:
                jmsg["functionParameters"]["correlationId"] = jmsg["correlationId"]
                self.functions[jmsg["functionId"]].implementation(
                    jmsg["functionParameters"]
                )
            else:
                logging.warning("Function could not be found: " + jmsg["functionId"])
        elif message.startswith("K"):
            jmsg = message.replace('\\"', '"')
            jmsg = json.loads(jmsg[2:])
            logging.info(str(jmsg))
            logging.debug("CONFIGURATION: " + str(jmsg))
            if jmsg["uuid"] == self.uuid:
                for key in jmsg["params"]:
                    if key in self.configuration["parameters"]:
                        self.changeConfigParameter(key, jmsg["params"][key])
                self.reRegister()

    def on_error(self, error):
        logging.error(error)

    def on_close(self):
        logging.debug("DISCONNECTED")
        self.connected = False
        self.registered = False
        if self.autoReconnect and not self.userDisconnect:
            logging.info(
                "### closed, waiting "
                + str(self.reconnectInterval)
                + " seconds before reconnect. ###"
            )
            time.sleep(self.reconnectInterval)
            self.reconnecting = True
            logging.info("Start reconnecting to msb url: >" + self.msb_url + "<")
            self.connect(self.msb_url)

    def on_open(self):
        logging.debug("Socket open")
        self.connected = True

    def enableDebug(self, debug=False):
        if debug:
            logging.basicConfig(
                format="[%(asctime)s] %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s"
            )
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.basicConfig(format="[%(asctime)s] %(message)s")
            logging.getLogger().setLevel(logging.INFO)
        self.debug = debug

    def enableTrace(self, trace=False):
        websocket.enableTrace(trace)

    def disableHostnameVerification(self, hostnameVerification=True):
        self.hostnameVerification = hostnameVerification

    def disableAutoReconnect(self, autoReconnect=False):
        self.autoReconnect = not autoReconnect

    def setReconnectInterval(self, interval=10000):
        self.reconnectInterval = interval / 1000

    def setEventCacheSize(self, eventCacheSize=True):
        self.eventCacheSize = eventCacheSize

    def enableThreadAsDaemon(self, threadAsDaemonEnabled=False):
        self.threadAsDaemonEnabled = threadAsDaemonEnabled

    def setKeepAlive(self, keepAlive=True, heartbeat_interval=8000):
        self.keepAlive = keepAlive
        if heartbeat_interval < 8000:
            self.heartbeat_interval = 8000
        else:
            self.heartbeat_interval = heartbeat_interval / 1000

    def _checkUrl(self, msb_url=None):
        server_id = str(randint(100, 999))
        session_id = str(uuid.uuid4()).replace("-", "")
        if msb_url is not None:
            self.msb_url = msb_url
        if "http://" in self.msb_url:
            self.msb_url = self.msb_url.replace("http://", "ws://")
        elif "https://" in self.msb_url:
            self.msb_url = self.msb_url.replace("https://", "wss://")
        if not (self.msb_url.startswith("ws://") or self.msb_url.startswith("wss://")):
            logging.error("WRONG MSB URL FORMAT: " + str(self.msb_url))
        if self.sockJsFraming:
            self._msb_url = (
                self.msb_url
                + "/websocket/data/"
                + server_id
                + "/"
                + session_id
                + "/websocket"
            )
        else:
            self._msb_url = self.msb_url + "/websocket/data/websocket"

    def connect(self, msb_url=None):
        self.userDisconnect = False

        self._checkUrl(msb_url)
        ws = websocket.WebSocketApp(
            self._msb_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws = ws
        ws.on_open = self.on_open

        def runf():
            try:
                if self.hostnameVerification:
                    if self.keepAlive:
                        ws.run_forever(
                            ping_interval=self.heartbeat_interval,
                            ping_timeout=self.heartbeat_interval - 5,
                            sslopt={
                                "cert_reqs": ssl.CERT_NONE,
                                "check_hostname": False,
                            },
                        )
                    else:
                        ws.run_forever(
                            sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False}
                        )
                else:
                    if self.keepAlive:
                        ws.run_forever(
                            ping_interval=self.heartbeat_interval,
                            ping_timeout=self.heartbeat_interval - 3,
                        )
                    else:
                        ws.run_forever()
            except Exception:
                pass

        logging.info("Connecting to MSB @ " + self.msb_url)
        wst = threading.Thread(target=runf)
        if self.threadAsDaemonEnabled:
            wst.setDaemon(True)
        wst.start()

    def disconnect(self):
        self.userDisconnect = True
        self.ws.close()

    def register(self):
        def _sendReg():
            if self.sockJsFraming:
                _selfd = json.dumps(
                    self.objectToJson(self.getSelfDescription())
                ).replace("\\n", "")
                _selfd = _selfd[1:-1]
                self.ws.send('["R ' + _selfd + '"]')
            else:
                self.ws.send("R " + self.objectToJson(self.getSelfDescription()))

        def _set_interval(func, sec):
            def func_wrapper():
                if self.connected:
                    func()
                else:
                    _set_interval(func, sec)

            t = threading.Timer(sec, func_wrapper)
            t.start()
            return t

        _set_interval(_sendReg, 0.1)

    def addEvent(
        self,
        event,
        event_name=None,
        event_description=None,
        event_dataformat=None,
        event_priority=0,
        isArray=None,
    ):
        if isArray:
            if isinstance(event_dataformat, ComplexDataFormat):
                event_dataformat.dataFormat["dataObject"]["type"] = "array"
                event_dataformat.dataFormat["dataObject"]["items"] = {}
                event_dataformat.dataFormat["dataObject"]["items"]["$ref"] = {}
                event_dataformat.dataFormat["dataObject"]["items"][
                    "$ref"
                ] = event_dataformat.dataFormat["dataObject"]["$ref"]
                del event_dataformat.dataFormat["dataObject"]["$ref"]
            if isinstance(event, Event):
                if vadilateEventDataFormat(event.dataFormat):
                    event.id = len(self.events) + 1
                    if event.eventId not in self.events:
                        self.events[event.eventId] = event
                    else:
                        logging.error(
                            str(event.eventId) + " already in events, change event id!"
                        )
            else:
                _event = Event(
                    event,
                    event_name,
                    event_description,
                    event_dataformat,
                    event_priority,
                    isArray,
                )
                if vadilateEventDataFormat(_event.dataFormat):
                    _event.id = len(self.events) + 1
                    if _event.eventId not in self.events:
                        self.events[_event.eventId] = _event
                    else:
                        logging.error(
                            str(_event.eventId) + " already in events, change event id!"
                        )
        else:
            if isinstance(event, Event):
                if vadilateEventDataFormat(event.dataFormat):
                    if event.isArray:
                        if "$ref" in event.dataFormat["dataObject"]:
                            event.dataFormat["dataObject"]["type"] = "array"
                            event.dataFormat["dataObject"]["items"] = {}
                            event.dataFormat["dataObject"]["items"]["$ref"] = {}
                            event.dataFormat["dataObject"]["items"][
                                "$ref"
                            ] = event.dataFormat["dataObject"]["$ref"]
                            del event.dataFormat["dataObject"]["$ref"]
                            event.id = len(self.events) + 1
                            if event.eventId not in self.events:
                                self.events[event.eventId] = event
                            else:
                                logging.error(
                                    str(event.eventId)
                                    + " already in events, change event id!"
                                )
                        else:
                            event.id = len(self.events) + 1
                            if event.eventId not in self.events:
                                self.events[event.eventId] = event
                            else:
                                logging.error(
                                    str(event.eventId)
                                    + " already in events, change event id!"
                                )
                    else:
                        event.id = len(self.events) + 1
                        if event.eventId not in self.events:
                            self.events[event.eventId] = event
                        else:
                            logging.error(
                                str(event.eventId)
                                + " already in events, change event id!"
                            )
            else:
                _event = Event(
                    event,
                    event_name,
                    event_description,
                    event_dataformat,
                    event_priority,
                    isArray,
                )
                if vadilateEventDataFormat(_event.dataFormat):
                    _event.id = len(self.events) + 1
                    if _event.eventId not in self.events:
                        self.events[_event.eventId] = _event
                    else:
                        logging.error(
                            str(_event.eventId) + " already in events, change event id!"
                        )

    def addFunction(
        self,
        function,
        function_name=None,
        function_description=None,
        function_dataformat=None,
        fnpointer=None,
        isArray=False,
        responseEvents=None,
    ):
        if isArray:
            if isinstance(function, Function):
                if isinstance(function_dataformat, ComplexDataFormat):
                    function_dataformat.dataFormat["dataObject"]["type"] = "array"
                    function_dataformat.dataFormat["dataObject"]["items"] = {}
                    function_dataformat.dataFormat["dataObject"]["items"]["$ref"] = {}
                    function_dataformat.dataFormat["dataObject"]["items"][
                        "$ref"
                    ] = function_dataformat.dataFormat["dataObject"]["$ref"]
                    del function_dataformat.dataFormat["dataObject"]["$ref"]
                if vadilateFunctionDataFormat(function.dataFormat):
                    if function.functionId not in self.functions:
                        self.functions[function.functionId] = function
                    else:
                        logging.error(
                            str(function.functionId)
                            + " already in functions, change event id!"
                        )

            else:
                _function = Function(
                    function,
                    function_name,
                    function_description,
                    function_dataformat,
                    fnpointer,
                    isArray,
                    responseEvents,
                )
                if vadilateFunctionDataFormat(_function.dataFormat):
                    if _function.functionId not in self.functions:
                        self.functions[_function.functionId] = _function
                    else:
                        logging.error(
                            str(_function.functionId)
                            + " already in functions, change event id!"
                        )
        else:
            if isinstance(function, Function):
                if vadilateFunctionDataFormat(function.dataFormat):
                    if function.isArray:
                        if "$ref" in function.dataFormat["dataObject"]:
                            function.dataFormat["dataObject"]["type"] = "array"
                            function.dataFormat["dataObject"]["items"] = {}
                            function.dataFormat["dataObject"]["items"]["$ref"] = {}
                            function.dataFormat["dataObject"]["items"][
                                "$ref"
                            ] = function.dataFormat["dataObject"]["$ref"]
                            del function.dataFormat["dataObject"]["$ref"]
                            if function.functionId not in self.functions:
                                self.functions[function.functionId] = function
                            else:
                                logging.error(
                                    str(function.functionId)
                                    + " already in functions, change event id!"
                                )
                        else:
                            if function.functionId not in self.functions:
                                self.functions[function.functionId] = function
                            else:
                                logging.error(
                                    str(function.functionId)
                                    + " already in functions, change event id!"
                                )
                    else:
                        if function.functionId not in self.functions:
                            self.functions[function.functionId] = function
                        else:
                            logging.error(
                                str(function.functionId)
                                + " already in functions, change event id!"
                            )
            else:
                _function = Function(
                    function,
                    function_name,
                    function_description,
                    function_dataformat,
                    fnpointer,
                    isArray,
                    responseEvents,
                )
                if vadilateFunctionDataFormat(_function.dataFormat):
                    if _function.functionId not in self.functions:
                        self.functions[_function.functionId] = _function
                    else:
                        logging.error(
                            str(_function.functionId)
                            + " already in functions, change event id!"
                        )

    def setEventValue(self, eventId, eventValue):
        if eventId in self.events:
            self.events[eventId].dataObject = eventValue

    def publish(
        self,
        eventId,
        dataObject=None,
        priority=None,
        cached=False,
        postDate=None,
        correlationId=None,
    ):
        event = {}
        if dataObject is not None:
            self.events[eventId].dataObject = dataObject
            event["dataObject"] = self.events[eventId].dataObject
        if priority is not None:
            self.events[eventId].priority = priority
        event["eventId"] = eventId
        event["uuid"] = self.uuid
        if correlationId is not None:
            event["correlationId"] = correlationId
        event["priority"] = self.events[eventId].priority
        if postDate is None:
            event["postDate"] = datetime.datetime.now().isoformat()

        if self.dataFormatValidation and dataObject is not None:
            if isinstance(self.events[eventId].df, ComplexDataFormat):
                schema = {}
                if "$ref" in self.events[eventId].dataFormat["dataObject"]:
                    schema["$ref"] = {}
                    schema["$ref"] = self.events[eventId].dataFormat["dataObject"][
                        "$ref"
                    ]
                    schema["type"] = "object"
                else:
                    schema["items"] = {}
                    schema["items"]["$ref"] = self.events[eventId].dataFormat[
                        "dataObject"
                    ]["items"]["$ref"]
                    schema["type"] = "array"
                schema["definitions"] = self.events[eventId].dataFormat
                try:
                    jsonschema.validate(
                        self.events[eventId].dataObject,
                        schema,
                        format_checker=jsonschema.FormatChecker(),
                    )
                except Exception as e:
                    logging.error(
                        "Error validating event "
                        + eventId
                        + ". Data object is of type "
                        + type(self.events[eventId].dataObject)
                    )
                    logging.error("Details: " + e)
                    return
            else:
                if not validateSimpleDataformat(
                    eventId,
                    self.events[eventId].df,
                    self.events[eventId].dataObject,
                    self.events[eventId].isArray,
                ):
                    return

        msg = self.objectToJson(event)
        if self.connected and self.registered:
            try:
                if self.sockJsFraming:
                    _msg = self.objectToJson(msg).replace("\\n", "")
                    self.ws.send('["E ' + _msg[1:-1] + '"]')
                else:
                    self.ws.send("E " + msg)
                logging.debug("SENDING: " + msg)
            except Exception:
                logging.exception(self, "Error, could not send message...")
                pass
        else:
            if self.eventCacheEnabled and cached:
                logging.debug(
                    "Not connected and/or registered, putting event in cache."
                )
                if len(self.eventCache) < self.eventCacheSize:
                    self.eventCache.append(msg)
                else:
                    self.eventCache.pop(0)
                    self.eventCache.append(msg)
            elif cached and not self.eventCacheEnabled:
                logging.debug(
                    "Global cache disabled, message cache flag overridden and discarded."
                )
            else:
                logging.debug("Caching disabled, message discarded.")

    def addConfigParameter(self, key, value, type):
        newParam = getDataType(type)
        newParam["type"] = newParam["type"].upper()
        if "format" in newParam:
            newParam["format"] = newParam["format"].upper()
        newParam["value"] = value
        # newParam['type'] = getConfigParamDataType(type)
        self.configuration["parameters"][key] = newParam

    def getConfigParameter(self, key):
        if key in self.configuration["parameters"]:
            return self.configuration["parameters"][key]["value"]
        else:
            return ""

    def changeConfigParameter(self, key, value):
        if key in self.configuration["parameters"]:
            self.configuration["parameters"][key]["value"] = value

    def reRegister(self):
        logging.debug("Reregistering after configuration parameter change...")
        if self.sockJsFraming:
            _selfd = json.dumps(self.objectToJson(self.getSelfDescription())).replace(
                "\\n", ""
            )
            self.ws.send('["R ' + _selfd[1:-1] + '"]')
        else:
            self.ws.send("R " + self.objectToJson(self.getSelfDescription()))

    def objectToJson(self, object):
        return jsonpickle.encode(object, unpicklable=False)

    def getSelfDescription(self):
        self_description = {}
        self_description["@class"] = self.service_type
        self_description["uuid"] = self.uuid
        self_description["name"] = self.name
        self_description["description"] = self.description
        self_description["token"] = self.token
        _ev = []
        e_props = ["@id", "id", "dataFormat", "description", "eventId", "name"]
        for event in self.events:
            current_e_props = []
            e = jsonpickle.decode(
                jsonpickle.encode(self.events[event], unpicklable=False)
            )
            for key in e.keys():
                if key == "id":
                    e["@id"] = e["id"]
                    del e[key]
            del e["priority"]
            del e["df"]
            if e["dataFormat"] is None:
                del e["dataFormat"]
            del e["isArray"]
            for key in e.keys():
                current_e_props.append(key)
            for key in current_e_props:
                if key not in e_props:
                    # logging.warning(self, 'Remove key from event if not event property valid in self description: ' + key)
                    try:
                        del e[key]
                    except Exception:
                        logging.exception(self, "Key not found: " + key)
            _ev.append(e)
        self_description["events"] = _ev
        _fu = []
        for function in self.functions:
            f = jsonpickle.decode(
                jsonpickle.encode(self.functions[function], unpicklable=False)
            )
            if f["responseEvents"] and len(f["responseEvents"]) > 0:
                _re = []
                for idx, re in enumerate(f["responseEvents"]):
                    _re.append(self.events[re].id)
                f["responseEvents"] = _re
            else:
                del f["responseEvents"]
            del f["isArray"]
            del f["implementation"]
            if f["dataFormat"] is None:
                del f["dataFormat"]
            _fu.append(f)
        self_description["functions"] = _fu
        self_description["configuration"] = self.configuration
        return self_description

    def readConfig(self):
        logging.info("Reading configuration from application.properties file")
        config = open("application.properties", "r")
        for line in config:
            configparam = line.split("=")
            if configparam[0] == "msb.type":
                self.service_type = configparam[1].rstrip()
            elif configparam[0] == "msb.name":
                self.name = configparam[1].rstrip()
            elif configparam[0] == "msb.uuid":
                self.uuid = configparam[1].rstrip()
            elif configparam[0] == "msb.token":
                self.token = configparam[1].rstrip()
            elif configparam[0] == "msb.url":
                self.msb_url = configparam[1].rstrip()
            elif configparam[0] == "msb.description":
                self.description = configparam[1].rstrip()


def getConfigParamDataType(dt):
    try:
        return str(getDataType(dt)["type"]).upper()
    except Exception:
        logging.exception("Unknown dataType: " + str(format))
        return "UNKNOWN_DATATYPE"


def vadilateEventDataFormat(df):
    if df is None:
        return True
    schema_file = os.path.join(os.path.dirname(__file__), "event_schema.json")
    schema = json.loads(open(schema_file).read())
    do = {"definitions": json.loads(jsonpickle.encode(df))}
    try:
        jsonschema.Draft4Validator(schema).validate(do)
    except Exception as e:
        logging.exception(e)
        return False
    return True


def vadilateFunctionDataFormat(df):
    if df is None:
        return True
    schema_file = os.path.join(os.path.dirname(__file__), "function_schema.json")
    schema = json.loads(open(schema_file).read())
    do = {"definitions": json.loads(jsonpickle.encode(df))}
    try:
        jsonschema.Draft4Validator(schema).validate(do)
    except Exception as e:
        logging.exception(e)
        return False
    return True


def validateSimpleDataformat(eventId, df, val, isArray):
    if isArray:
        try:
            if all((type(item) == df) for item in val):
                return True
            else:
                logging.error(
                    "Error validating event "
                    + eventId
                    + ": "
                    + "Value in list doesn't fit the required data format: "
                    + str(val)
                    + " = "
                    + str(type(val))
                    + ", expected: "
                    + str(df)
                )
                return False
        except Exception:
            logging.error(
                "Error validating event "
                + eventId
                + ". DataObject ("
                + str(val)
                + ") is not an array as defined."
            )
            return False
    else:
        if type(val) == df:
            return True
    logging.error(
        "Error validating event "
        + eventId
        + ": "
        + "Value doesn't fit the required data format: "
        + str(val)
        + " = "
        + str(type(val))
        + ", expected: "
        + str(df)
    )
    return False
