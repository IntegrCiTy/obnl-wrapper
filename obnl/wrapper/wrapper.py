import logging

from obnl.message.default_pb2 import MetaMessage
from obnl.message.coside.coside_pb2 import *

from ict.connection.node import Node
from obnl.core.impl.server import Scheduler
from obnl.wrapper.util import convert_protobuf_to_data


class Wrapper(Node):
    def __init__(self, host, vhost, username, password, config_file="wrappers.json"):
        super().__init__(host, vhost, username, password, config_file)

        self._init_onbl = None
        self._schedule = None

        self._scheduler = None

    def on_cosim(self, ch, method, props, body):
        Node.LOGGER.info(self._name + " receives a cosim message.")
        m = MetaMessage()
        m.ParseFromString(body)

        if m.details.Is(SimulationInit.DESCRIPTOR):
            sim = SimulationInit()
            m.details.Unpack(sim)

            self._init_onbl = convert_protobuf_to_data(sim)

        elif m.details.Is(Schedule.DESCRIPTOR):

            sch = Schedule()
            m.details.Unpack(sch)

            self._schedule = convert_protobuf_to_data(sch)

        elif m.details.Is(StartSimulation.DESCRIPTOR):
            self.LOGGER.debug("Have to start the simulation")
            if self._init_onbl and self._schedule:
                self.LOGGER.debug("Initialisation is OK")

                self._scheduler = Scheduler(self.host, 'obnl_vhost', 'obnl', 'obnl',
                                            'scheduler.json',
                                            self._init_onbl, self._schedule,
                                            log_level=logging.DEBUG)
                self.LOGGER.debug("RUN")
                self._scheduler.start()

        self._channel.basic_ack(delivery_tag=method.delivery_tag)
