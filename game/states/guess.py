import pygame as pg

from game.data import GameData
from game.display import Display
from game.state import State, Transition, TransitionType
from game.widgets import Button, Text


class GuessState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)
        self.__data = data

        self.__text = Text(
            pg.Rect(
                self.__display.resolution[0] // 2 - 150,
                self.__display.resolution[1] // 2 - 50,
                400,
                40,
            ),
            "Guesser, é par ou ímpar?",
            (255, 255, 255),
        )

        self.__submit1 = Button(
            pg.Rect(
                self.__display.resolution[0] // 2 - 250,
                self.__display.resolution[1] // 2 + 50,
                100,
                40,
            ),
            "Par",
        )

        self.__submit2 = Button(
            pg.Rect(
                self.__display.resolution[0] // 2 + 150,
                self.__display.resolution[1] // 2 + 50,
                100,
                40,
            ),
            "ímpar",
        )

        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(self.__surface, (0, 0, 0), self.__surface.get_rect())
        self.__text.draw(self.__surface)
        self.__submit1.draw(self.__surface)
        self.__submit2.draw(self.__surface)

    def execute(self):
        self.__display.draw(self.__surface)
        return Transition(TransitionType.NONE)
