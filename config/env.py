import os


def get(key, default=None):
    var = os.environ.get(key=key, default=default)
    if isinstance(var, str):
        if var.lower() == 'true':
            var = True
        elif var.lower() == 'false':
            var = False
    return var


BROWSER = 'chrome'  # browser name ["chrome", "edge", "firefox", "remote"]
SEND_REPORT = os.environ.get('SEND_REPORT', default=True)
CREATE_ALLURE_REPORT = False
