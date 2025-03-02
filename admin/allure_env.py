import os.path
from datetime import datetime

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY

from config.env import BROWSER

allure_path = os.path.join(CURRENT_DIRECTORY, "allure-results", f"{BROWSER}")
env_path = 'environment.properties'
get_full_path = os.path.join(allure_path, env_path)


def get_environment():
    today = datetime.now()
    time_now = today.strftime("%Y/%m/%d %H:%M:%S")
    with open(get_full_path, 'w') as file:
        file.write('os_platform = linux'
                   f'\nos_browser = {BROWSER}'
                   f'\ndate = {time_now}')
    print("\nenvironment.properties file added")
    print("\n", get_full_path)
