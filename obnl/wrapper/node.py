import logging
import threading

from ict.connection.node import Node

from obnl.core.impl.server import Scheduler
from obnl.wrapper.util import convert_protobuf_to_data

from ict.protobuf.simulation_pb2 import SimulationInit, Schedule, StartSimulation
from ict.protobuf.core_pb2 import MetaMessage


class WrapperNode(Node):
    def __init__(self, host, vhost, username, password, obnl_pass,
                 config_file="wrappers.json", obnl_file='scheduler.json'):
        super().__init__(host, vhost, username, password, config_file)

        self._obnl_password = obnl_pass
        self._obnl_file = obnl_file

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
            if self._init_onbl and self._schedule:

                self._scheduler = Scheduler(self.host, 'obnl_vhost', 'obnl', self._obnl_password,
                                            self._obnl_file,
                                            self._init_onbl, self._schedule,
                                            log_level=logging.DEBUG)
                threading.Thread(self._scheduler.start()).start()

        self._channel.basic_ack(delivery_tag=method.delivery_tag)
