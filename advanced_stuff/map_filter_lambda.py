def positive_even_squares(*args):
    lst = []
    for i in args:
        lst += filter(lambda x: x > 0 and x % 2 == 0, i)
    return list(map(lambda x: x**2, lst))
