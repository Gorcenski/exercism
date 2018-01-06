from math import pow


def is_armstrong(number):
    return number == sum([pow(int(x), len(str(number))) for x in str(number)])
