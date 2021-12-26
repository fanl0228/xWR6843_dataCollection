import subprocess
import time
from IWR6843_PKG.Loging import Logger

log = Logger("DCA1000EVM_CLI")

#local CLI
# PATH_BASE = r"D:/xWR6843_DCA1000_GetData/DCA1000EVM_CLI"
# DCA1000EVM_CLI_Control = PATH_BASE + r"/DCA1000EVM_CLI_Control.exe "
PATH_BASE = os.path.join(os.getcwd(), "DCA1000EVM_CLI")
DCA1000EVM_CLI_Control = os.path.join(PATH_BASE, "DCA1000EVM_CLI_Control.exe ")
CWD_DIR = PATH_BASE

global JSON_FILE

def dca1000_set_json_file(json):
    global JSON_FILE
    # JSON_FILE = PATH_BASE + r"/" + json
    JSON_FILE = json

def dca1000_reset_ar_device():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" reset_ar_device " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_fpga():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" fpga " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_record():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" record " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_fpga_version():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" fpga_version " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_dll_version():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" dll_version " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_cli_version():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" cli_version " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_start_record():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" start_record " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    # output, error = result.communicate()
    # log.debug(output)
    # if error is not None:
    #     log.error(error)


def dca1000_stop_record():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" stop_record " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_query_sys_status():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" query_sys_status " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_help():
    if JSON_FILE == None:
        print("ERROR: json file is none!")
        return
    result = subprocess.Popen(DCA1000EVM_CLI_Control + r" -h " + JSON_FILE,
                              cwd=CWD_DIR,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              encoding='utf-8')
    output, error = result.communicate()
    log.debug(output)
    if error is not None:
        log.error(error)


def dca1000_config_all():
    # config
    dca1000_reset_ar_device()
    dca1000_fpga()
    dca1000_record()

    # get version
    dca1000_fpga_version()
    dca1000_cli_version()
    dca1000_cli_version()
