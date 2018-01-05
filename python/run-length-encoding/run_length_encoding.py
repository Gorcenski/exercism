from itertools import groupby
from re import findall


def decode(text):
    r = ''.join([(int(x) * y[0]) + y[1:] for x, y in
                zip(findall(r'\d+', text),
                    findall(r'[^((?!\d).)*$]+', text))])

    return r if r else text


def encode(text):
    def compact_ones(num):
        return '' if num == 1 else str(num)

    return ''.join([compact_ones(sum(1 for q in y)) + x
                   for x, y in groupby(text)])
