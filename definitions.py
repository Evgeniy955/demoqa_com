import os

def get(key, default=None):
    return os.environ.get(key=key, default=default)


# __________________EDITABLE CONFIGURATION__________________
BROWSER = get("BROWSER", "chrome")  # browser name
ENVIRONMENT = get("ENVIRONMENT", "ROW_NONPROD")  # ROW_NONPROD, CN_NONPROD, ROW_PROD, CN_PROD
IS_HIDDEN_PROD = get("HIDDEN_PROD", False)
LANGUAGE = get("LANGUAGE", "EN")
REGION = get("REGION", "United States")  # China, Ukraine, United States
# If you need another region update REGIONS = { ... } and REGION_TRANSLATIONS = { ... }
# __________________________________________________________


# REGION_TRANSLATIONS = {
#     "United States": UNITED_STATES_REGION[LANGUAGE],
#     "Ukraine": UKRAINE_REGION[LANGUAGE],
#     "China": CHINA_REGION[LANGUAGE],
# }
#
# LANGUAGES_TRANSLATIONS = {
#     "EN": ENGLISH_LANGUAGE[LANGUAGE],
#     "CHI": CHINESE_SIMPLIFIED_LANGUAGE[LANGUAGE],
#     "ES": SPANISH_LANGUAGE[LANGUAGE],
#     "DE": GERMAN_LANGUAGE[LANGUAGE],
#     "FR": FRENCH_LANGUAGE[LANGUAGE],
# }

LANGUAGE_URL_PARAM = {"EN": "", "ES": "es", "CHI": "zh-hans", "FR": "fr", "DE": "de"}

LOCALE_CODE = {"EN": "en,en_US", "CHI": "zh-cn,zh_CN", "ES": "es,es_ES", "DE": "de,de_DE", "FR": "fr,fr_FR"}

URLS = {
    "ROW_NONPROD": {
        "CORPSITE": "https://corpsite.nonprod.3d4medical.com",
        "ACCOUNTS": "https://accounts.nonprod.3d4medical.com",
        "WEB_STORE": "https://store.nonprod.3d4medical.com",
        "COOKIES": "https://cookies.nonprod.3d4medical.com",
        "CA_SERVER": "https://ca.nonprod.3d4medical.com",
        "CMD_URL": "https://cb.nonprod.3d4medical.com",
    },
    "ROW_PROD": {
        "CORPSITE": "https://3d4medical.com",
        "ACCOUNTS": "https://accounts.3d4medical.com",
        "WEB_STORE": "https://store.3d4medical.com",
        "COOKIES": "https://cookies.3d4medical.com",
        "CA_SERVER": "https://ca.3d4medical.com",
        "CMD_URL": "https://cb.3d4medical.com",
    },
    "CN_NONPROD": {
        "CORPSITE": "https://corpsite.nonprod.completeanatomy.cn",
        "ACCOUNTS": "https://accounts.nonprod.completeanatomy.cn",
        "WEB_STORE": "https://store.nonprod.completeanatomy.cn",
        "COOKIES": "https://cookies.nonprod.completeanatomy.cn",
        "CA_SERVER": "https://ca.nonprod.completeanatomy.cn",
        "CMD_URL": "https://cb.nonprod.completeanatomy.cn",
        "MINISTRY_OF_INFORMATION": "https://beian.miit.gov.cn/",
    },
    "CN_PROD": {
        "CORPSITE": "https://completeanatomy.cn",
        "ACCOUNTS": "https://accounts.completeanatomy.cn",
        "WEB_STORE": "https://store.completeanatomy.cn",
        "COOKIES": "https://cookies.completeanatomy.cn",
        "CA_SERVER": "https://ca.completeanatomy.cn",
        "CMD_URL": "https://cb.completeanatomy.cn",
        "MINISTRY_OF_INFORMATION": "https://beian.miit.gov.cn/",
    },
    "SUPPORT_HUB": {
        "EN": "https://service.elsevier.com",
        "ES": "https://es.service.elsevier.com",
        "ZH": "https://cn.service.elsevier.com",
    },
    "CONTACT_SALES": "https://www.elsevier.com",
    "HELP_CENTER": "https://3d4medical.zendesk.com",
}

CMD_URL = get("CMD_URL", URLS["ROW_NONPROD"]["CMD_URL"])
CMD_URLS = {
    "CMD MAIN PAGE": CMD_URL,
    "CMD LOGIN": f"{CMD_URL}/dashboard/login/",
    "CMD DASHBOARD": f"{CMD_URL}/dashboard/",
    "CMD placeholder": "",
}

CREDIT_CARD = get("NON_PROD", "4242 4242 4242 4242")

PAYPAL_NON_PROD = {
    # this is a real gmail account
    # password from ca , paypal and gmail is identical
    "login": "purchase.test.ca@gmail.com",
    "password": get("PASSWORD"),
}


PASSWORD = get("PASSWORD")

STORE_CREDENTIALS = {
    "user_for_password_reset": {
        "ROW_NONPROD": {"User": "row.user.for.login@gmail.com", "Password": PASSWORD},
        "CN_NONPROD": {"User": "cntestuserforlogin@gmail.com", "Password": PASSWORD},
    },
    "default_user_without_subscriptions": {
        "ROW_NONPROD": {"User": "row.default.user.without.sub@gmail.com", "Password": PASSWORD},
        "CN_NONPROD": {"User": "cn.default.user.without.sub@gmail.com", "Password": PASSWORD},
    },
}

CMD_CREDENTIALS = {
    "CMD Edu": {"User": "test_cmd_edu@3d4medical.com", "Password": PASSWORD, "ca_id": 55718, "sso_id": 2937},
    "CMD Edu without groups": {
        "User": "test_cmd_edu_without_groups@3d4medical.com",
        "Password": PASSWORD,
        "ca_id": 55757,
        "sso_id": 2998,
    },
    "CMD StuPlus": {"User": "test_cmd_stu@3d4medical.com", "Password": PASSWORD, "ca_id": 55719, "sso_id": 2938},
    "CMD StuPlus 1": {"User": "test_cmd_stu_1@3d4medical.com", "Password": PASSWORD, "ca_id": 55765, "sso_id": 3015},
    # TODO: Add several more testing accounts for the future automation
    "CMD StuPlus 2": {"User": "test_cmd_stu_2@3d4medical.com", "Password": PASSWORD, "ca_id": 0000, "sso_id": 0000},
    "CMD StuPlus 3": {"User": "test_cmd_stu_3@3d4medical.com", "Password": PASSWORD, "ca_id": 0000, "sso_id": 0000},
    "CMD StuPlus 4": {"User": "test_cmd_stu_4@3d4medical.com", "Password": PASSWORD, "ca_id": 0000, "sso_id": 0000},
    "CMD StuPlus 5": {"User": "test_cmd_stu_5@3d4medical.com", "Password": PASSWORD, "ca_id": 0000, "sso_id": 0000},
    "CMD No Progress": {
        "User": "test_cmd_no_progress@3d4medical.com",
        "Password": PASSWORD,
        "ca_id": 56240,
        "sso_id": 3672,
    },
}
