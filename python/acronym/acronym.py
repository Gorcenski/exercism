def abbreviate(words):
    return ''.join([x[0].upper() for x in words.replace('-', ' ').split(' ')])
