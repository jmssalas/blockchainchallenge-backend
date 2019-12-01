VALID_CODES = ['ORG0001', 'ENV001', 'PAP001', 'RES001', 'VID001']
CODE_TRASH_TYPE = {'ORG0001': 1, 'ENV001': 2, 'PAP001': 3, 'RES001': 4, 'VID001': 5}


def validate(code):
    return code in VALID_CODES


def trash_type(code):
    return CODE_TRASH_TYPE[code]
