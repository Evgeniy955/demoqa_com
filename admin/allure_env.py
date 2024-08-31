import platform
from datetime import datetime

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY

from config.env import BROWSER


def get_os_type():
    os_type = platform.system()
    if os_type == "Windows":
        return "Windows"
    elif os_type == "Darwin":
        return "macOS"
    elif os_type == "Linux":
        return "Ubuntu"
    else:
        return "Your OS is not supported"


folder_path = CURRENT_DIRECTORY + f'/allure-results/{BROWSER}'
env_property_path = '/environment.properties'

if get_os_type() == "Windows":
    allure_path = folder_path.replace("/", "\\")
    env_path = env_property_path.replace("/", "\\")
else:
    allure_path = folder_path
    env_path = env_property_path

def get_environment():
    today = datetime.now()
    time_now = today.strftime("%Y/%m/%d %H:%M:%S")
    with open(allure_path + env_path, 'w') as file:
        file.write('os_platform = linux'
                   f'\nos_browser = {BROWSER}'
                   f'\ndate = {time_now}')
    print("environment.properties file added")
