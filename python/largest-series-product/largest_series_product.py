from functools import reduce


def largest_product(series, size):
    if size > len(series):
        raise ValueError("""No consecutive
            substrings of length {}.""".format(size))
    if size < 0:
        raise ValueError("Cannot have negative length substring.")

    # extract the substrings of length at most size
    s = [list(series[i:i + size]) for i in range(len(series))]

    # Because of the default behavior of reduce, the following can be empty
    # if and only if the series is empty and the size is empty
    products = [reduce(lambda x, y: x * int(y), t, 1)
                for t in s if len(t) == size]

    return max(products) if products else 1
