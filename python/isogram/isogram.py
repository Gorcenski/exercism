import string


def is_isogram(str):
    alpha = set(string.lowercase[:26])
    str = [val for val in str.lower() if val in alpha]
    return len(str) == len(set(str))
