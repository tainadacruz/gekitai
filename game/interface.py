import sys

import pygame as pg

from game.board import Board
from game.constants import FRAMERATE, RESOLUTION, Color, Status


class Interface:
    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode(RESOLUTION, pg.RESIZABLE | pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED, 32)
        self.__board = Board()
        self.__clock = pg.time.Clock()
        self.draw()
        self.run()

    def run(self) -> None:
        while True:
            self.__clock.tick(FRAMERATE)
            self.loop()
            pg.display.update()

    def write_text(self, text: str, position: tuple[int, int]) -> None:
        font = pg.font.Font(None, 32)
        surface = font.render(text, False, (0, 0, 0))
        self.__screen.blit(
            surface,
            (position[0] - (surface.get_width() // 2), position[1] - (surface.get_height() // 2))
        )

    def draw(self):
        self.__screen.fill((255, 255, 255))

        cell_image = pg.image.load("assets/cell.png")
        red_piece = pg.image.load("assets/red_piece.png")
        blue_piece = pg.image.load("assets/blue_piece.png")
        logo = pg.image.load("assets/logo.png")

        self.__screen.blit(logo, (0, 0))
        self.__screen.blit(red_piece, (0, 384 + 50))
        self.__screen.blit(blue_piece, (384 - 64, 384 + 50))

        red = self.__board.get_player(Color.RED)
        blue = self.__board.get_player(Color.BLUE)

        self.write_text(str(red.get_piece_count()), (64, 448))
        self.write_text(str(blue.get_piece_count()), (384 - 64, 448))

        if self.__board.get_status() == Status.NO_MATCH:
            self.write_text("Clique para iniciar a partida", (self.__screen.get_width() // 2, 516))
        elif self.__board.get_status() == Status.FINISHED:
            winner = self.__board.get_winner()
            if winner is not None:
                self.write_text(f"Vencedor: {winner}", (self.__screen.get_width() // 2, 516))
            else:
                self.write_text("Empate!", (self.__screen.get_width() // 2, 516))
        elif self.__board.get_status() == Status.IN_PROGRESS:
            turn = self.__board.current_player()
            self.write_text(f"Vez do {turn}", (self.__screen.get_width() // 2, 516))

        for x in range(6):
            for y in range(6):
                self.__screen.blit(cell_image, (x * 64, y * 64 + 50))
                cell = self.__board.get_cell((x, y))
                if cell.is_occupied():
                    piece = cell.get_piece()
                    self.__screen.blit(
                        red_piece if piece.get_color() == Color.RED else blue_piece,
                        (x * 64, y * 64 + 50),
                    )

    def loop(self):
        if (position := self.get_input()) != None:
            if (position[0] == 1 or 0) and position[1] == 8:
                self.exit()
            self.__board.click(position)
            self.draw()

    def get_input(self) -> tuple[int, int]:
        """Aguarda um click na tela"""
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                i, j = pg.mouse.get_pos()
                position = (i // 64, (j - 50) // 64)
                return position
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def exit(self):
        pg.quit()
        sys.exit()
            
