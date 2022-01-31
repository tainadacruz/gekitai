import pygame as pg
import sys

from game.board import Board
from game.constants import FRAMERATE, RESOLUTION, Color
from game.interface import Interface
from game.player import Player


def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode(
        RESOLUTION, pg.RESIZABLE | pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED, 32
    )

    interface = Interface(screen)

    while True:
        clock.tick(FRAMERATE)

        interface.loop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()


if __name__ == "__main__":
    main()
