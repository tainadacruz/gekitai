from game.constants import Color
from game.exceptions import NoPiecesException
from game.piece import Piece


class Player:
    def __init__(self, color: Color):
        self.__pieces = [Piece(color) for _ in range(8)]
        self.__color = color

    @property
    def piece_count(self) -> int:
        return len(self.__pieces)

    @property
    def color(self) -> Color:
        return self.__color

    def place_piece(self) -> Piece:
        if self.piece_count > 0:
            return self.__pieces.pop()
        else:
            # Jogo já devia ter sido encerrado
            raise NoPiecesException()

    def retrieve_piece(self, piece: Piece):
        self.__pieces.append(piece)
