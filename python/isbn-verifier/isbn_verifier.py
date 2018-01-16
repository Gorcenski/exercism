import string


def verify(isbn):
    trans = str.maketrans('', '', string.punctuation)
    isbn = str.translate(isbn, trans).lower()

    if not set(isbn).issubset(set(string.digits + 'x')) or len(isbn) != 10:
        return False
    if 'x' in isbn and isbn.find('x') < len(isbn) - 1:
        return False

    vals = [int(c) if c != 'x' else 10 for c in isbn]

    return not sum([a * b for a, b in zip(vals, reversed(range(11)))]) % 11
