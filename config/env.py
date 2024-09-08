import os

from cmdline_add_args.allure_report_path import get_os_type


def get(key, default=None):
    var = os.environ.get(key, default)
    if isinstance(var, str):
        if var.lower() == 'true':
            var = True
        elif var.lower() == 'false':
            var = False
    return var


# local variables
if get_os_type() != "Windows":
    # block for macOS, Ubuntu
    BROWSER = get('BROWSER', 'chrome')  # browser name ["chrome", "edge", "firefox", safari (local only)]
    CREATE_ALLURE_REPORT = get('CREATE_ALLURE_REPORT', False)
    SEND_REPORT = get('SEND_REPORT', False)
else:
    # block for Windows
    BROWSER = "chrome"
    CREATE_ALLURE_REPORT = False
    SEND_REPORT = False


LOCAL_RUN = get('LOCAL_RUN', True)