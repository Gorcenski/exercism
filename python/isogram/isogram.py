import string


def is_isogram(str):
    alpha = set(string.ascii_lowercase)
    str = [val for val in str.lower() if val in alpha]
    return len(str) == len(set(str))
