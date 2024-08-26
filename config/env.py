import os


def get(key, default=None):
    var = os.environ.get(key=key, default=default)
    if isinstance(var, str):
        if var.lower() == 'true':
            var = True
        elif var.lower() == 'false':
            var = False
    return var


BROWSER = get("BROWSER", "chrome")
CREATE_ALLURE_REPORT = get('CREATE_ALLURE_REPORT', True)
