def flatten_lists(func):
    def wrapper(*args):
        lst = []
        for i in args:
            if isinstance(i, list):
                lst.extend(i)
            else:
                lst.append(i)
        return func(*lst)
    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        lst = []
        for i in args:
            if isinstance(i, str) and i.isdigit():
                lst.append(int(i))
            else:
                lst.append(i)
        return func(*lst)
    return wrapper


def filter_integers(func):
    def wrapper(*args):
        lst = []
        for i in args:
            if isinstance(i, int):
                lst.append(i)
        return func(*lst)
    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)
