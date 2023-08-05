import asyncio
import logging
import traceback
import nats.aio.client
from nats.aio.errors import ErrTimeout
import json
import socket
from datetime import datetime, timezone
from dateutil import parser
from .errors import *
from ._modes import function_mode_old, process_mode
from ._version import __version__

logging.basicConfig(
    format=u'%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO
)


class scanner_wrapper:
    non_json_serializable_fields = (
        "tls",
        "worker_function",
        "input_handler",
        "output_handler"
    )
    config = {
        # This args more important
        "tls": None,
        "worker_function": None,
        # Return array of args for process. Calling: input_handler(data, meta)
        "input_handler": None,
        # Processing lines from process. Return array with results. Calling: output_handler(line)
        # Line - not decoded
        "output_handler": None,
        # Set in\out or do not use it. Set fields which needs to start
        "fields_in": [],
        "fields_out": [],
        # TODO login password etc
        # FLAGS --------------
        "send_meta": True,
        # each result from array will be sended directly to NATS
        "send_raw": False,
        # output handler must take array with lines if chunked_send not True
        # collect all output of module and send to your handler function
        "chunked_send": False,
        # result must be DICT! and then its added to previous
        "add_result_to_data": False,
        # Process lines or bytes
        "readline": False,
        # print out stderr from procee or not
        "print_stderr": False,
        # receive only one message or all from NATS queue
        "one_message_receive": True,
        "check_expired": True,
        # the next word in pipeline put into worker as arg
        "pipeline_arg": False,
        # module registration in webAPI
        "registration": True
    }
    # when you subscribes to two queues may been created two processes
    # control that with semaphore
    sem = asyncio.Semaphore(1)

    def __init__(self, **kwargs):
        if "name" not in kwargs:
            raise ModuleNameError()

        self.nc = nats.aio.client.Client()
        self.config.update(kwargs)

        self.config["hostname"] = socket.gethostname()
        if self.config["hostname"] == "":
            raise NoHostnameError()

    def decode_msg(self, msg):
        """Decode messages from NATS
        Return json objects with data and meta
        Return cur_pipeline
        """
        task_raw = msg.data.decode()
        task = json.loads(task_raw)
        return task["data"], task["meta"]

    async def nats_report_publisher(self, meta, result_array, **kwargs):
        """
        Send messages to NATS.
        :param meta: meta info from nats
        :param result_array: each of result will be sent to nats
        :param kwargs: args sents too
        """
        package = {"data": {}, "meta": meta}
        package["meta"]["timestamp"] = datetime.now(timezone.utc).timestamp()
        package["meta"]["cur_scanner"] = self.config["name"]
        package["meta"]["lib_version"] = __version__

        for key, value in kwargs.items():
            package["meta"][key] = value
        if result_array:
            for result in result_array:
                if self.config["send_raw"]:
                    await self.nc.publish("_reporter", result)
                else:
                    package["data"] = result
                    await self.nc.publish("_reporter", json.dumps(package).encode())
        else:
            await self.nc.publish("_reporter", json.dumps(package).encode())

    async def subscribe_on_one_msg(self, name, queue, callback):
        """
        Subscrbe to NATS for only one message
        :param name:
        :param queue:
        :param callback:
        :return: sid
        """
        sid = await self.nc.subscribe(name, queue, cb=callback, is_async=True)
        await self.nc.auto_unsubscribe(sid, 1)
        return sid

    @staticmethod
    def task_time_is_expired(meta):
        if meta["start_time"]:
            start_time = parser.parse(meta["start_time"])
            return (datetime.now(timezone.utc) - start_time).seconds > int(meta["max_working_time"])
        return False

    async def _run(self, loop):
        async def disconnected_cb():
            logging.info("Got disconnected!")

        async def reconnected_cb():
            # See who we are connected to on reconnect.
            logging.info("Got reconnected to " +
                         str(self.nc.connected_url.netloc))

        async def error_cb(e):
            logging.error("There was an error: " + traceback.format_exc())

        async def closed_cb():
            logging.info("Connection is closed")

        async def connect():
            """

            :return:
            """
            while not self.nc.is_connected:
                try:
                    await self.nc.connect(**options)
                    logging.info("Connected to NATS %s.", self.nc.connected_url.netloc)
                    # logging.info("Subscribe to: '%s', '%s', '%s'", self.config["name"],
                    #              self.config["name"] + self.config["hostname"], self.config["name"] + ".>")
                except nats.aio.client.ErrNoServers as e:
                    logging.error("Could not connect to any server in cluster.")
                    logging.error(traceback.format_exc())

        async def message_handler(msg):
            """Create another process from args send output to output_handler(output_line)
            and then calling result_publisher
            """
            with (await self.sem):
                status = None
                cur_pipeline = msg.subject
                try:
                    data, meta = self.decode_msg(msg)

                    logging.info("Received from '%s':", cur_pipeline)
                    logging.info("Meta: '%s'", meta)
                    logging.info("Data: '%s'", data)

                    new_pipeline = ".".join(cur_pipeline.split(".")[1:])

                    # Task begin report
                    if self.config["send_meta"]:
                        await self.nats_report_publisher(
                            meta,
                            [],
                            current_status="begin",
                        )
                        logging.info("Begin report has been sended.")
                        # Fix no time for send. Swap context to await.
                        await asyncio.sleep(0)

                    try:
                        if self.config["check_expired"] and scanner_wrapper.task_time_is_expired(meta):
                            raise ExpiredTimeError()
                        if self.config["worker_function"]:
                            await function_mode_old(self, data, meta, new_pipeline)
                        elif self.config["input_handler"] and self.config["output_handler"]:
                            await process_mode(self, data, meta, new_pipeline)
                        else:
                            raise NotEnoughArgsError()

                    except NotEnoughArgsError as e:
                        raise NotEnoughArgsError()

                    except BadPackageDataError as e:
                        status = "error.bad_package"
                        logging.error("Bad Package")

                    except ExpiredTimeError as expired:
                        status = "error.task_expired"
                        logging.warning("Received task with expired time!")

                    except Exception as e:
                        status = "error.bad_worker"
                        logging.error(
                            "Exception in worker! Report will be sended!")
                        logging.error(traceback.format_exc())

                    # Task end report
                    if status:
                        if self.config["send_meta"]:
                            await self.nats_report_publisher(
                                meta,
                                [],
                                current_status=status,
                            )
                            logging.info("Error status report has been sended.")

                    if self.config["send_meta"]:
                        await self.nats_report_publisher(
                            meta,
                            [],
                            current_status="end",
                        )
                        logging.info("End report has been sended.")

                except Exception as e:
                    logging.error("Unexpected exception in main logic!!!")
                    logging.error(traceback.format_exc())

                if self.config["one_message_receive"]:
                    # resub on one message mechanism
                    if cur_pipeline == self.config["name"]:
                        resub_pipeline = self.config["name"]
                        resub_queue = self.config["name"]
                    elif cur_pipeline == self.config["name"] + self.config["hostname"]:
                        resub_pipeline = self.config["name"] + self.config["hostname"]
                        resub_queue = self.config["name"] + self.config["hostname"]
                    else:
                        resub_pipeline = self.config["name"] + ".>"
                        resub_queue = self.config["name"]
                    await self.subscribe_on_one_msg(
                        resub_pipeline,
                        resub_queue,
                        message_handler
                    )

        async def subscribe(name, unique_name, one_message_receive):
            """
            Subscribe to NATS channels:
                name
                name.>
                unique_name
            on one message or message flow
            :param name: string `masscan`
            :param unique_name: string `lkhkbjn`
            :param one_message_receive: bool default `True`
            :return:
            """
            if one_message_receive:
                await self.subscribe_on_one_msg(
                    name,
                    name,
                    message_handler
                )
                await self.subscribe_on_one_msg(
                    name + ".>",
                    name,
                    message_handler
                )
                await self.subscribe_on_one_msg(
                    unique_name,
                    unique_name,
                    message_handler
                )
            else:
                await self.nc.subscribe(
                    name,
                    name,
                    cb=message_handler,
                    is_async=True
                )
                await self.nc.subscribe(
                    name + ".>",
                    name,
                    cb=message_handler,
                    is_async=True
                )
                await self.nc.subscribe(
                    unique_name,
                    unique_name,
                    cb=message_handler,
                    is_async=True
                )
            logging.info("Subscribe to %s, %s, %s", name, name + ".>", unique_name)

        # Configuring nats
        options = {
            # Setup pool of servers from a NATS cluster.
            "servers": self.config['nats'],
            "tls": self.config['tls'],
            "name": self.config['name'],
            "io_loop": loop,
            # Will try to connect to servers in order of configuration,
            # by defaults it connect to one in the pool randomly.
            "dont_randomize": True,
            # Optionally set reconnect wait and max reconnect attempts.
            # This example means 10 seconds total per backend.
            # Next two lines configure client to try to reconnect approximately 7 days ( 8960 * 10 )- 7 days in seconds
            "max_reconnect_attempts": 8960,
            "reconnect_time_wait": 3,
            # Setup callbacks to be notified on disconnects and reconnects
            "disconnected_cb": disconnected_cb,
            "reconnected_cb": reconnected_cb,
            # Setup callbacks to be notified when there is an error
            # or connection is closed.
            "error_cb": error_cb,
            "closed_cb": closed_cb,
        }

        logging.info("Started module named '{name}'.".format(name=self.config["name"]))
        logging.info("Nats module wrapper. Version '%s'", __version__)

        await connect()

        if self.nc.is_connected:
            # register request
            unique_name = self.config["name"] + self.config["hostname"]
            if self.config["registration"]:
                while True:
                    try:
                        register_data = json.dumps({key: value for key, value in self.config.items() if
                                                    key not in self.non_json_serializable_fields})
                        register_response = await self.nc.request("_registration", register_data.encode(), 1)
                        register_response = json.loads(register_response.data.decode())
                        unique_name = register_response["unique_name"]
                        logging.info("Module registered! Module unique_name is: %s", unique_name)
                        break
                    except ErrTimeout:
                        logging.warning("Module registration is not possible! The registrar is not responding.")
                    await asyncio.sleep(10, loop=loop)

                options["name"] = unique_name

                logging.info("Module will be reconnected to change name!")
                await self.nc.close()
                await connect()

            await subscribe(self.config["name"], options["name"], self.config["one_message_receive"])

            while True:
                if not self.nc.is_connected:
                    await self.nc.close()
                    await connect()
                    await subscribe(self.config["name"], options["name"], self.config["one_message_receive"])
                await asyncio.sleep(5, loop=loop)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run(loop))
        loop.close()
