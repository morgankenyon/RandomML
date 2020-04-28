import copy
import enum

class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o


MARKER_TO_CHAR = {
    None: ' . ',
    Player.x: ' x ',
    Player.o: ' o ',
}