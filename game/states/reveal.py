import pygame as pg

from game.data import GameData
from game.display import Display
from game.state import State, Transition, TransitionType


class RevealState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)
        self.__data = data

        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(self.__surface, (0, 255, 0), self.__surface.get_rect())

    def execute(self):
        self.__display.draw(self.__surface)
        return Transition(TransitionType.NONE)
