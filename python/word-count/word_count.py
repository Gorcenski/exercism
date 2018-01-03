import string


def word_count(phrase):
    trans = str.maketrans({'_': ' ', ',': ' ', '\n': ' ', '\t': ' ', ':': ''})
    words = [w.strip(string.punctuation)
             for w in phrase.translate(trans).lower().split()]
    return {w: words.count(w) for w in set(words)}
