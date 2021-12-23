import time
import serial
import serial.tools.list_ports
from .Loging import Logger

data_timeout = 0.000015  # timeout for 921600 baud; 0.00000868055 for a byte


class serial_iwr6843():
    def __init__(self, configFileName="configs/profile_2d.cfg", userPort="COM3", dataPort="COM5"):
        self.log=Logger("serial")
        self.config = configFileName
        self.userPort = userPort
        self.dataPort = dataPort
        self.userPort_obj = None
        self.dataPort_obj = None

        self.data_buffer = b''
        self.data_chunk_size = 32  # this MUST be 32 for TLV to work without magic number
        self.data_buffer_max_size = 3200

    def get_user_port(self):
        return self.userPort_obj

    def get_data_port(self):
        return self.dataPort_obj

    def serial_open(self):
        # support check serial port
        # todo
        # self._serial_check_port()

        # Open the serial ports for the configuration and the data ports
        try:
            # CLI port cannot have timeout because the stream is user-programmed
            self.userPort_obj = serial.Serial(self.userPort, 115200, parity=serial.PARITY_NONE,
                                              stopbits=serial.STOPBITS_ONE,timeout=0.3)
            if(not self.userPort_obj.isOpen()):
                self.log.error("cliport is not open: {}".format(self.userPort))

            self.dataPort_obj = serial.Serial(self.dataPort, 921600, parity=serial.PARITY_NONE,
                                              stopbits=serial.STOPBITS_ONE, timeout=0.025)
            if(not self.dataPort_obj.isOpen()):
                 self.log.error("dataPort is not open: {}}".format(self.dataPort))

        except serial.SerialException as se:
            # self.serial_close()
            raise Exception('Serial Port Occupied, error = ' + str(se))


        # Read the configuration file and send it to the board
        config = [line.rstrip('\r\n') for line in open(self.config)]
        for line in config:
            self.userPort_obj.write((line + '\r').encode())
            time.sleep(0.2)
            ack = self.userPort_obj.readline()
            self.log.debug(ack)

        time.sleep(3)
        cli_result = self.userPort_obj.read(self.userPort_obj.in_waiting).decode()
        self.log.debug(cli_result)  # CLI output of the board



    def serial_sensor_start(self):
        self.userPort_obj.write(('sensor Start \n').encode())
        result = self.userPort_obj.read(self.userPort_obj.in_waiting).decode()
        self.log.debug(result)

    def serial_sensor_stop(self):
        self.userPort_obj.write(('sensor Stop \n').encode())
        result = self.userPort_obj.read(self.userPort_obj.in_waiting).decode()
        self.log.debug(result)

    def serial_close(self):
        self.userPort_obj.close()
        self.dataPort_obj.close()

    def serial_clear_buffer(self):
        self.userPort_obj.reset_input_buffer()
        self.userPort_obj.reset_output_buffer()
        self.dataPort_obj.reset_input_buffer()
        self.dataPort_obj.reset_output_buffer()

    def serial_initialize(self):
        self.serial_open()
        time.sleep(1)
        self.serial_clear_buffer()
        time.sleep(1)
        self.serial_sensor_start()

    def _serial_check_port(self):
        port_list = list(serial.tools.list_ports.comports())
        for com in port_list:
            des = com.description
            if -1 != des.rfind("User", beg=0, end=len(com.description)-len('User')):
                # com is user port
                if self.userPort != com.name:
                    self.log.error("Please Check XDS110 Class Application/User UART is: " + com.name)

            if -1 != des.rfind("Data", beg=0, end=len(com.description) - len('Data')):
                # com is user port
                if self.dataPort != com.name:
                    self.log.error("Please Check XDS110 Class Data Port is: " + com.name)