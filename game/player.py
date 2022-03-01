from game.constants import Color
from game.exceptions import NoPiecesException
from game.piece import Piece


class Player:
    def __init__(self, color: Color):
        self.__pieces = [Piece(color) for _ in range(8)]
        self.__color = color

    def get_color(self) -> Color:
        return self.__color

    def place_piece(self) -> Piece:
        if self.has_pieces():
            return self.__pieces.pop()
        else:
            raise NoPiecesException()

    def take_piece(self, piece: Piece):
        self.__pieces.append(piece)

    def has_pieces(self) -> bool:
        return len(self.__pieces) > 0

    def get_piece_count(self) -> int:
        return len(self.__pieces)