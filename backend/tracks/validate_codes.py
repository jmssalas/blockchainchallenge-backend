VALID_CODES = ['JFK123', 'WX362V', '04LMK3', 'RD09OJ', 'CIC3K4']
CODE_TRASH_TYPE = {'JFK123': 1, 'WX362V': 2, '04LMK3': 3, 'RD09OJ': 4, 'CIC3K4': 5}


def validate(code):
    return code in VALID_CODES


def trash_type(code):
    return CODE_TRASH_TYPE[code]