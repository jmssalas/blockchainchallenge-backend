VALID_CODES = [
    'ORG001', 'ORG002', 'ORG003', 'ORG004',
    'ENV001', 'ENV002', 'ENV003', 'ENV004',
    'PAP001', 'PAP002', 'PAP003', 'PAP004',
    'RES001', 'RES002', 'RES003', 'RES004',
    'VID001', 'VID002', 'VID003', 'VID004']


def validate(code):
    return code in VALID_CODES


def trash_type(code):
    if 'ORG' in code:
        return 1
    if 'ENV' in code:
        return 2
    if 'PAP' in code:
        return 3
    if 'RES' in code:
        return 4
    if 'VID' in code:
        return 5



