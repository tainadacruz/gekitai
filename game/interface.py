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

    def draw(self):
        self.__screen.fill((255, 255, 255))
        cell_image = pg.image.load("assets/cell.png")
        red_piece = pg.image.load("assets/red_piece.png")
        blue_piece = pg.image.load("assets/blue_piece.png")
        logo = pg.image.load("assets/logo.png")
        font = pg.font.Font(None, 64)
        font_smaller = pg.font.Font(None, 32)
        exit_button = pg.image.load("assets/exit.png")
        start_button = pg.image.load("assets/start.png")

        self.__screen.blit(logo, (0, 0))
        self.__screen.blit(red_piece, (0, 384 + 50))
        self.__screen.blit(blue_piece, (384 - 64, 384 + 50))
        self.__screen.blit(exit_button, (0, 384 + 180))
        self.__screen.blit(start_button, (334 - 80, 384 + 180))

        red = self.__board.get_player(Color.RED)
        blue = self.__board.get_player(Color.BLUE)

        self.__screen.blit(
            font.render(str(red.get_piece_count()), False, (0, 0, 0)), (64 + 20, 384 + 50 + 12)
        )
        self.__screen.blit(
            font.render(str(blue.get_piece_count()), False, (0, 0, 0)), (384 - 128 + 20, 384 + 50 + 12)
        )

        if self.__board.get_winner() == False:
            self.__screen.blit(
                font.render("", False, (0, 0, 0)), (384 - 40 + 20, 384 + 50 + 12)
            )
        else:
            if len(self.__board.get_winner()) == 1:
                vencedor = self.__board.get_winner()[0].get_color()
                if vencedor == Color.BLUE:
                    vencedor = "Azul" 
                else:
                    vencedor = "Vermelho"
                self.__screen.blit(
                    font_smaller.render(f"Vencedor: {vencedor}", False, (0, 0, 0)), (384 - 290, 384 + 50 + 12 + 70)
                )
            else:
                self.__screen.blit(
                    font_smaller.render("Empate!", False, (0, 0, 0)), (384 - 238, 384 + 50 + 12 + 70)
                )


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
            
