import pygame as pg
from game.constants import DIRECTIONS
from game.exceptions import InvalidPositionException

from game.piece import Piece
from game.constants import Color
from game.player import Player


class Board:
    def __init__(self, screen: pg.Surface, players: list[Player]):
        self.__screen = screen
        self.__board: list[list[Piece]] = [[None] * 6 for _ in range(6)]
        self.__players = players
        self.__draw_board()

    def __draw_board(self):
        cell = pg.image.load("assets/cell.png")
        red_piece = pg.image.load("assets/red_piece.png")
        blue_piece = pg.image.load("assets/blue_piece.png")

        for x in range(6):
            for y in range(6):
                self.__screen.blit(cell, (x * 100, y * 100))
                if not self.position_empty((x, y)):
                    piece = self.__board[x][y]
                    self.__screen.blit(
                        red_piece if piece.color == Color.RED else blue_piece,
                        (x * 100 + 10, y * 100 + 10),
                    )

    def position_valid(self, position: tuple[int, int]) -> bool:
        return 0 <= position[0] < 6 and 0 <= position[1] < 6

    def position_empty(self, position: tuple[int, int]) -> bool:
        i, j = position
        return self.__board[i][j] == None

    def loop(self):
        if (position := self.get_input()) != None:
            piece = self.__players[0].place_piece()
            self.place_piece(position, piece)
            self.__players.reverse()

    def get_input(self) -> tuple[int, int]:
        """Aguarda um click no tabuleiro"""
        if pg.event.peek(eventtype=pg.MOUSEBUTTONDOWN):
            i, j = pg.mouse.get_pos()
            position = (i // 100, j // 100)
            if self.position_valid(position) and self.position_empty(position):
                return position

    def place_piece(self, position: tuple[int, int], piece: Piece):
        if not self.position_valid(position):
            raise InvalidPositionException()

        i, j = position
        self.__board[i][j] = piece

        removed_pieces: list[Piece] = []

        for direction in DIRECTIONS:
            i = position[0] + direction[0]
            j = position[1] + direction[1]
            if self.position_valid((i, j)) and not self.position_empty((i, j)):
                push = (i + direction[0], j + direction[1])
                if not self.position_valid(push):
                    removed_pieces.append(self.__board[i][j])
                    self.__board[i][j] = None
                elif self.position_empty(push):
                    self.__board[push[0]][push[1]] = self.__board[i][j]
                    self.__board[i][j] = None

        for removed in removed_pieces:
            owner: Player = next(
                p for p in self.__players if p.color == removed.color
            )
            owner.take_piece(removed)

        self.__draw_board()
