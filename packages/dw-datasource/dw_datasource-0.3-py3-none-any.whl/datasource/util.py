
def retry(f):
    """
    Wrapper function to retry an operation
    :param f:
    :param n_attempts:
    :return:
    """
    n_attempts = 3
    def wrapper(*args, **kwargs):
        for i in range(n_attempts):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                if i == n_attempts - 1:
                    raise e
    return wrapper


def ascii(utf_str):
    if utf_str is None or isinstance(utf_str, str):
        return utf_str

    return utf_str.decode('ascii')
