import string


def encode(plain_text):
    trans = str.maketrans(string.ascii_lowercase,
                          ''.join(reversed(string.ascii_lowercase)),
                          string.punctuation)
    rev = str.translate(plain_text.lower(), trans).replace(' ', '')
    return ' '.join([rev[i:i + 5] for i in range(0, len(rev), 5)])


def decode(ciphered_text):
    trans = str.maketrans(''.join(reversed(string.ascii_lowercase)),
                          string.ascii_lowercase)
    return str.translate(ciphered_text.replace(' ', ''), trans)
