from .vxi11interface import Vxi11Interface

from srsgui import Instrument
from srsgui.inst import TcpipInterface, SerialInterface
from srsgui.task.inputs import ComPortListInput, IntegerListInput, BoolInput, \
                               Ip4Input, IntegerInput

from .components import Stream


class SR865(Instrument):
    _IdString = 'SR865'

    available_interfaces = [
        [
            Vxi11Interface,
            {
                'ip_address': Ip4Input('192.168.1.10'),
            }
        ],

        [
            TcpipInterface,
            {
                'ip_address': Ip4Input('192.168.1.10'),
                'port': 23
            }
        ],

        [
            SerialInterface,
            {
                'port': ComPortListInput(),
                'baud_rate': IntegerListInput([300, 1200, 2400, 4800, 9600, 19200,
                                               38400, 115200, 230400, 460800], 7)
            }
        ],
    ]

    def __init__(self, interface_type=None, *args):
        super().__init__(interface_type, *args)

        self.stream = Stream(self)

    def connect(self, interface_type, *args):
        super().connect(interface_type, *args)
        if isinstance(self.comm, TcpipInterface):
            print(self.query_text(''))  # Read out the initial string
