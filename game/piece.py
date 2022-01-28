import pygame as pg


from game.constants import Color


class Piece:
    """Peça do jogo"""

    def __init__(self, color: Color):
        self.__color = color

    @property
    def color(self) -> Color:
        return self.__color
