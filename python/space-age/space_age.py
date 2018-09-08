from enum import Enum

class OrbitalRatio(Enum):
    EARTH = 1
    MERCURY = 0.2408467
    VENUS = 0.61519726
    MARS = 1.8808158
    JUPITER = 11.862615
    SATURN = 29.447498
    URANUS = 84.016846
    NEPTUNE = 164.79132

class SpaceAge(object):
    SECONDS_IN_YEAR = 31557600

    def __init__(self, seconds):
        self.seconds = seconds
        for name, member in OrbitalRatio.__members__.items():
            _method = self._make_method(member.value)
            setattr(self, "on_" + name.lower(), _method)

    def _make_method(self, value):
        def _method():
            return round(self.seconds / self.SECONDS_IN_YEAR / value, 2)
        return _method
