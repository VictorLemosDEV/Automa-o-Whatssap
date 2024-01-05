import re

def is_phone_valid(phone_number):
    PHONE_NUMBER_REGEX = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

    isValid = bool(re.search(PHONE_NUMBER_REGEX, phone_number))

    return isValid