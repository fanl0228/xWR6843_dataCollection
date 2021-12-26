# xWR6843_DCA1000_GetData

## Function 

The main functions of the repository are as follows:

    - Use serial port to send cfg parameters to xWR6843 
    - Use DCA1000EVM_CLI_Control.exe to configure DCA1000 parameters
    - Start/stop DCA1000 to collect data


## How to Use it？
    - Download this repository to D:
    - Create "logs" and "RadarDate" directories
    - pip install requirement.txt
    - modify IWR6843_PKG/configs/profile_2d.cfg (If needed), but must ensure the parameter “lvdsStreamCfg -1 0 1 0”
    - modify serial port
    - IWR6843 is configured as DCA1000 capture card mode


## Reference

1. [Ti](https://www.ti.com/)
2. 
