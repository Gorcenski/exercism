import string


def word_count(phrase):
    trans = str.maketrans({'_': ' ', ',': ' ', '\n': ' ', '\t': ' ', ':': ''})
    li = [w.strip(string.punctuation)
          for w in phrase.translate(trans).lower().split()]
    print(li)
    return {w: li.count(w) for w in set(li)}
