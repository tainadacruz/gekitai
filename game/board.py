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
        self.draw()

    def draw(self):
        self.__screen.fill((255, 255, 255))
        cell = pg.image.load("assets/cell.png")
        red_piece = pg.image.load("assets/red_piece.png")
        blue_piece = pg.image.load("assets/blue_piece.png")
        logo = pg.image.load("assets/logo.png")
        font = pg.font.Font(None, 64)

        self.__screen.blit(logo, (0, 0))
        self.__screen.blit(red_piece, (0, 384 + 50))
        self.__screen.blit(blue_piece, (384 - 64, 384 + 50))
        self.__screen.blit(
            font.render("8", False, (0, 0, 0)), (64 + 20, 384 + 50 + 12)
        )
        self.__screen.blit(
            font.render("8", False, (0, 0, 0)), (384 - 128 + 20, 384 + 50 + 12)
        )

        for x in range(6):
            for y in range(6):
                self.__screen.blit(cell, (x * 64, y * 64 + 50))
                if not self.position_empty((x, y)):
                    piece = self.__board[x][y]
                    self.__screen.blit(
                        red_piece if piece.color == Color.RED else blue_piece,
                        (x * 64, y * 64 + 50),
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
            position = (i // 64, (j - 50) // 64)
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

        self.draw()
