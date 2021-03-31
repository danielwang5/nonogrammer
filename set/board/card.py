from enum import IntEnum

class Card:
    def __init__(self, color, shape, texture, count):
        self.color = color
        self.shape = shape
        self.texture = texture
        self.count = count

class CardColor(IntEnum):
    RED = 0
    GREEN = 1
    PURPLE = 2

class CardShape(IntEnum):
    DIAMOND = 0
    PILL = 1
    SQUIGGLE = 2

class CardTexture(IntEnum):
    HOLLOW = 0
    STRIPED = 1
    SOLID = 2

class CardCount(IntEnum):
    ONE = 0
    TWO = 1
    THREE = 2