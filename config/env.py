import os


def get(key, default=None):
    var = os.environ.get(key=key, default=default)
    if isinstance(var, str):
        if var.lower() == 'true':
            var = True
        elif var.lower() == 'false':
            var = False
    return var


BROWSER: bool = get('BROWSER', 'firefox')  # browser name ["chrome", "edge", "firefox", "remote"]
CREATE_ALLURE_REPORT: bool = get('CREATE_ALLURE_REPORT', False)
SEND_REPORT: bool = get('SEND_REPORT', False)
