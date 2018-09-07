import math
from functools import reduce

def numeral(number):
    if number > 3000:
        raise ValueError("Numbers over 3000 not supported by Rome")

    ONES = "IXCM"
    FIVES = "VLD"

    def numeralify(value, base):
        f = '' if base >= len(FIVES) else FIVES[base]
        if value % 5 == 4:
            return ONES[base] + (ONES[base + 1] if value > 5 else f)

        return f * (value >= 5) + ONES[base] * ((value - 5) % 5)

    n = int(math.log10(number))
    return reduce(lambda x,y: x + y,
                  [numeralify(number // 10**(n-i) % 10, n-i) for i in range(n+1)],
                  '')
