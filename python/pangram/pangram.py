import string


def is_pangram(input=''):
    alphabet = set(string.ascii_lowercase)
    return set(input.lower()).intersection(alphabet) == alphabet
