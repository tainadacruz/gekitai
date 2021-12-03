import pygame as pg
from game.constants import DIRECTIONS
from game.exceptions import InvalidPositionException

from game.piece import Piece


class Board:
    def __init__(self):
        self.__board: list[list[Piece]] = [[None] * 6 for _ in range(6)]
        self.__surface = pg.Surface((600, 600))
        self.__draw_board()

    def __draw_board(self):
        cell = pg.image.load("assets/cell.png")

        for x in range(6):
            for y in range(6):
                self.__surface.blit(cell, (x * 100, y * 100))
                if not self.position_empty((x, y)):
                    piece = self.__board[x][y]
                    self.__surface.blit(
                        piece.sprite, (x * 100 + 10, y * 100 + 10)
                    )

    @property
    def surface(self) -> pg.Surface:
        return self.__surface

    def position_valid(self, position: tuple[int, int]):
        return 0 <= position[0] < 6 and 0 <= position[1] < 6

    def position_empty(self, position: tuple[int, int]):
        i, j = position
        return self.__board[i][j] == None

    def get_input(self):
        """Aguarda um click no tabuleiro"""
        if pg.event.peek(eventtype=pg.MOUSEBUTTONDOWN):
            i, j = pg.mouse.get_pos()
            position = ((i - 200) // 100, j // 100)
            if self.position_valid(position) and self.position_empty(position):
                return position

    def place_piece(self, position: tuple[int, int], piece: Piece):
        if not self.position_valid(position):
            raise InvalidPositionException()
        i, j = position
        self.__board[i][j] = piece

        pieces = []

        for direction in DIRECTIONS:
            i = position[0] + direction[0]
            j = position[1] + direction[1]
            if self.position_valid((i, j)) and not self.position_empty((i, j)):
                push = (i + direction[0], j + direction[1])
                if not self.position_valid(push):
                    pieces.append(self.__board[i][j])
                    self.__board[i][j] = None
                elif self.position_empty(push):
                    self.__board[push[0]][push[1]] = self.__board[i][j]
                    self.__board[i][j] = None

        self.__draw_board()

        return pieces
