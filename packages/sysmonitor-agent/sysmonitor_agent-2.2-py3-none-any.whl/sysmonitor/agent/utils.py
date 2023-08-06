"""Utilities used by us"""

import string
import random


def random_str(length=30, alphanumeric=True):
    """
    Generate a random string

    :param int length: string lenght
    :param bool alphanumeric: If True, string will be alphanumeric
    :return: Random string
    :rtype: str
    """
    chars = string.ascii_letters
    if alphanumeric:
        chars += string.digits

    return "".join(random.choice(chars) for _ in range(length))


def str_to_bool(value):
    """
    Convert a string to boolean

    :param string value: String to convert
    :return: Converted boolean value
    :rtype: bool
    """
    if not isinstance(value, str):
        return False
    value = value.strip().lower()
    return True if value in ["true", "yes", "1", "y"] else False


def merge_dicts(*dicts):
    """
    Merge multiple dicts into one

    :param dict dicts: Dictionaries to merge
    :return: merged dictionaries
    :rtype: dict
    """
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

def str_to_list(value, separator=","):
    """
    Convert a string into a list based on separator

    :param string value: String to split
    :param string separator: Separator used to split string
    :return: Splited string
    :rtype: list
    """
    return [x.strip() for x in value.split(separator) if x]
