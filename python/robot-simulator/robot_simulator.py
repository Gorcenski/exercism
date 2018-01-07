# Globals for the bearings
# Change the values as you see fit
EAST = complex(1, 0)
NORTH = complex(0, 1)
WEST = complex(-1, 0)
SOUTH = complex(0, -1)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing *= complex(0, -1)

    def turn_left(self):
        self.bearing *= complex(0, 1)

    def advance(self):
        self.coordinates = tuple(a + b for a, b in
                                 zip(self.coordinates,
                                     (self.bearing.real, self.bearing.imag)))

    def simulate(self, commands):
        mapping = {'R': self.turn_right,
                   'L': self.turn_left,
                   'A': self.advance}
        for c in commands:
            if c in mapping:
                mapping[c]()
            else:
                raise ValueError("Unknown Command {}".format(c))
