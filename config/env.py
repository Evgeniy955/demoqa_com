import os


def get(key, default=None):
    var = os.environ.get(key=key, default=default)
    if isinstance(var, str):
        if var.lower() == 'true':
            var = True
        elif var.lower() == 'false':
            var = False
    return var


current_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
ALLURE_REPORT_PATH = get('ALLURE_REPORT_PATH', current_directory)
ALLURE_RESULTS = os.path.join(current_directory, 'allure-results')
BROWSER = get("BROWSER", "chrome")  # browser name ["chrome" "edge", "firefox", "remote"]

CREATE_ALLURE_REPORT = get('CREATE_ALLURE_REPORT', False)

# -v -s --alluredir=allure_results
