from enum import Enum


class Items(Enum):
    EGGS = 1
    PEANUTS = 2
    SHELLFISH = 4
    STRAWBERRIES = 8
    TOMATOES = 16
    CHOCOLATE = 32
    POLLEN = 64
    CATS = 128


class Allergies(object):
    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return (self.score & Items[item.upper()].value) > 0

    @property
    def lst(self):
        return [x.name.lower() for x in Items if (self.score & x.value) > 0]
