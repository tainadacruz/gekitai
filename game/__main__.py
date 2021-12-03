import pygame as pg
import sys

from game.board import Board
from game.constants import FRAMERATE, RESOLUTION, Color
from game.player import Player


def main():
    clock = pg.time.Clock()
    window = pg.display.set_mode(
        RESOLUTION, pg.RESIZABLE | pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED, 32
    )

    current_player = Player(Color.RED)
    waiting_player = Player(Color.BLUE)
    board = Board()

    while True:
        clock.tick(FRAMERATE)

        if (position := board.get_input()) != None:
            piece = current_player.place_piece()
            print(position, piece)
            board.place_piece(position, piece)
            current_player, waiting_player = waiting_player, current_player

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        window.fill((255, 255, 255))
        window.blit(board.surface, (200, 0))
        pg.display.update()


if __name__ == "__main__":
    main()
