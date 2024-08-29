from datetime import datetime

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY

from config.env import BROWSER

folder_path = CURRENT_DIRECTORY + f'\\allure-results\\{BROWSER}'


def get_environment():
    today = datetime.now()
    time_now = today.strftime("%Y/%m/%d %H:%M:%S")
    with open(folder_path + '\\environment.properties', 'w') as file:
        file.write('os_platform = linux'
                   f'\nos_browser = {BROWSER}'
                   f'\ndate = {time_now}')
