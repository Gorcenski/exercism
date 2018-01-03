import string


def hey(phrase):
    if (phrase == phrase.upper()) and \
       set(phrase).intersection(string.ascii_uppercase):
        return "Whoa, chill out!"
    elif phrase.split() == []:
        return "Fine. Be that way!"
    elif list(phrase.rstrip())[-1] == '?':
        return "Sure."
    else:
        return "Whatever."
