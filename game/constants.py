from enum import Enum, auto


FRAMERATE = 30.0
RESOLUTION = (384, 600)
DIRECTIONS = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]


class Color(Enum):
    RED = auto()
    BLUE = auto()
