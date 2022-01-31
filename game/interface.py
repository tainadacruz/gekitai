import pygame as pg
from game.board import Board

from game.constants import Color


class Interface:
    def __init__(self, screen: pg.Surface, board: Board):
        self.__screen = screen
        self.__board = board
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
                if not self.__board.position_empty((x, y)):
                    piece = self.__board.at((x, y))
                    self.__screen.blit(
                        red_piece if piece.color == Color.RED else blue_piece,
                        (x * 64, y * 64 + 50),
                    )

    def loop(self):
        if (position := self.get_input()) != None:
            piece = self.__board.current_player.place_piece()
            self.__board.place_piece(position, piece)
            self.__board.flip_players()
            self.draw()

    def get_input(self) -> tuple[int, int]:
        """Aguarda um click na tela"""
        if pg.event.peek(eventtype=pg.MOUSEBUTTONDOWN):
            i, j = pg.mouse.get_pos()
            position = (i // 64, (j - 50) // 64)
            if self.__board.position_valid(
                position
            ) and self.__board.position_empty(position):
                return position
