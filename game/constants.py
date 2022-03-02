from enum import Enum, auto


FRAMERATE = 30.0
RESOLUTION = (384, 640)
DIRECTIONS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1), (0, 1),   (1, 1),
]


class Color(Enum):
    RED = auto()
    BLUE = auto()


class Status(Enum):
    NO_MATCH = auto()
    IN_PROGRESS = auto()
    FINISHED = auto()