from functools import reduce


def get_symmetric(*args):
    flatten_list = reduce(lambda a, b: a + b, args)

    symmetric_list = []

    flatten_list = set(flatten_list)

    for n in flatten_list:
        occurrences = 0
        for row in args:
            for col in set(row):
                if col == n:
                    occurrences += 1

        if occurrences == 1:
            symmetric_list.append(n)

    return sorted(symmetric_list)
