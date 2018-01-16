from enum import Enum


class Numerals(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class TensBase(Enum):
    TWENTY = 20
    THIRTY = 30
    FORTY = 40
    FIFTY = 50
    SIXTY = 60
    SEVENTY = 70
    EIGHTY = 80
    NINETY = 90


class TensSpecial(Enum):
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14
    FIFTEEN = 15
    SIXTEEN = 16
    SEVENTEEN = 17
    EIGHTEEN = 18
    NINETEEN = 19


class Magnitudes(Enum):
    THOUSAND = 1e3
    MILLION = 1e6
    BILLION = 1e9


def get_name(enumerable, value):
    return next((x.name.lower() for x in enumerable if x.value == value), '')


def say(number):
    def get_hundreds(chunk):
        h = chunk // 100
        return get_name(Numerals, h) + " hundred" if h > 0 else ''

    def get_tens(chunk):
        r = chunk % 100
        if r >= 10 and r <= 19:
            return get_name(TensSpecial, r)
        else:
            s = r % 10
            tens = get_name(TensBase, r - s)
            ones = get_name(Numerals, s) if s else ''
            return '-'.join([x for x in [tens, ones] if x])

    def parse(chunk):
        """Process a number up to 999 inclusive and parse it to English"""
        return ' and '.join([x for x in [get_hundreds(chunk), get_tens(chunk)]
                             if x])

    if number < 0:
        raise ValueError("Argument {} is negative.".format(number))
    elif number > 1e12 - 1:
        raise ValueError("Argument {} is too large.".format(number))

    text = ''
    base = 1
    while number >= 1:
        chunk = number % 1e3
        # necessary for joining a number less than 100 with
        # a number greater than 999, e.g. one thousand and two
        conj = 'and' if base == 1 and chunk < 100 and number > 1e3 else ''
        segment = parse(chunk)
        mag = get_name(Magnitudes, base)

        if segment:
            text = ' '.join(x for x in [conj, segment, mag, text] if x)

        base *= 1e3
        number //= 1e3

    return text if text else 'zero'
