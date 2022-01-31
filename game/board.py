from game.constants import DIRECTIONS
from game.exceptions import InvalidPositionException

from game.piece import Piece
from game.player import Player


class Board:
    def __init__(self, players: list[Player]):
        self.__cells: list[list[Piece]] = [[None] * 6 for _ in range(6)]
        self.__players = players

    @property
    def current_player(self) -> Player:
        return self.__players[0]

    def flip_players(self) -> None:
        self.__players.reverse()

    def at(self, position: tuple[int, int]) -> Piece:
        if self.position_valid(position):
            i, j = position
            return self.__cells[i][j]
        return None

    def position_valid(self, position: tuple[int, int]) -> bool:
        return 0 <= position[0] < 6 and 0 <= position[1] < 6

    def position_empty(self, position: tuple[int, int]) -> bool:
        i, j = position
        return self.__cells[i][j] == None

    def place_piece(self, position: tuple[int, int], piece: Piece):
        if not self.position_valid(position):
            raise InvalidPositionException()

        i, j = position
        self.__cells[i][j] = piece

        removed_pieces: list[Piece] = []

        for direction in DIRECTIONS:
            i = position[0] + direction[0]
            j = position[1] + direction[1]
            if self.position_valid((i, j)) and not self.position_empty((i, j)):
                push = (i + direction[0], j + direction[1])
                if not self.position_valid(push):
                    removed_pieces.append(self.__cells[i][j])
                    self.__cells[i][j] = None
                elif self.position_empty(push):
                    self.__cells[push[0]][push[1]] = self.__cells[i][j]
                    self.__cells[i][j] = None

        for removed in removed_pieces:
            owner: Player = next(
                p for p in self.__players if p.color == removed.color
            )
            owner.take_piece(removed)
