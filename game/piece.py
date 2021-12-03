import pygame as pg


from game.constants import Color


class Piece:
    """Peça do jogo"""

    def __init__(self, color: Color):
        self.__sprite = pg.image.load(
            "assets/red_piece.png"
            if color == Color.RED
            else "assets/blue_piece.png"
        )

    @property
    def sprite(self) -> pg.Surface:
        return self.__sprite
