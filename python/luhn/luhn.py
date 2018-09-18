import re
import math

class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')
        pass

    def is_valid(self):
        if re.search(r'\D', self.card_num) or len(self.card_num) == 1:
            return False

        def convert_num(x):
            return 2 * x if x <= 4 else 2 * x - 9

        n = len(self.card_num)
        return not sum([int(self.card_num[-i-1]) if i % 2 == 0
                        else convert_num(int(self.card_num[-i-1]))
                        for i in range(n)]) % 10
        pass
