from collections import Counter

YACHT = lambda x: all(i == x[0] for i in x) * 50
ONES = lambda x: x.count(1)
TWOS = lambda x: x.count(2) * 2
THREES = lambda x: x.count(3) * 3
FOURS = lambda x: x.count(4) * 4
FIVES = lambda x: x.count(5) * 5
SIXES = lambda x: x.count(6) * 6
FULL_HOUSE = lambda x: (sorted(Counter(x).values()) == [2, 3]) * sum(x)
FOUR_OF_A_KIND = lambda x: sum([(x.count(n) >= 4) * 4 * n for n in set(x)])
LITTLE_STRAIGHT = lambda x: ((len(set(x)) == 5) & (sum(x) == 15)) * 30
BIG_STRAIGHT = lambda x: ((len(set(x)) == 5) & (sum(x) == 20)) * 30
CHOICE = sum

def score(dice, category):
    return category(dice)
