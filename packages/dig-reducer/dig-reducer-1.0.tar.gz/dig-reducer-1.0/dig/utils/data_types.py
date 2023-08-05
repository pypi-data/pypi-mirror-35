

def is_str(value):
    if isinstance(value, str): # or isinstance(value, unicode):
        return True
    return False


def is_list(value):
    if isinstance(value, list) or isinstance(value, tuple):
        return True
    return False


def is_dict(value):
    if isinstance(value, dict):
        return True


def to_list(value):
    if is_list(value):
        return value
    else:
        return [value]


def str_compare(a, b):
    return ((a > b) - (a < b))
