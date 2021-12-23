#-*- coding: UTF-8 -*-

import time
from DCA1000EVM_CLI import dca1000_cli_cmd
from IWR6843_PKG import mmwave_serial

if __name__ == '__main__':
    # config DCA1000EVM
    dca1000_json = "datacard_config_recoder_raw_default.json"
    dca1000_cli_cmd.dca1000_set_json_file(json=dca1000_json)
    dca1000_cli_cmd.dca1000_config_all()
    time.sleep(2)

    # config IWR6843 and sensor start
    config_file_name = "IWR6843_PKG/configs/profile_2d.cfg"
    iwr6843 = mmwave_serial.serial_iwr6843(configFileName=config_file_name,
                                           userPort="COM24", dataPort="COM23")
    iwr6843.serial_initialize()
    time.sleep(2)

    # DCA1000EVM start record
    dca1000_cli_cmd.dca1000_start_record()

    time.sleep(60)
    dca1000_cli_cmd.dca1000_stop_record()
    iwr6843.serial_sensor_stop()
    # iwr6843.serial_close()