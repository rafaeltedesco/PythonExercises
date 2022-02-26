from functools import reduce


def flat_list(args):
    return reduce(lambda a, b: a + b, args)


def count_ocurrencies(flatten_list, args):
    for n in flatten_list:
        ocurrencies = 0
        for row in args:
            for col in set(row):
                if col == n:
                    ocurrencies += 1
        yield ocurrencies, n


def get_symmetric(*args):
    flatten_list = set(flat_list(args))

    symmetric_list = []
    for ocurrencies, n in count_ocurrencies(flatten_list, args):
        if ocurrencies == 1:
            symmetric_list.append(n)

    return sorted(symmetric_list)
