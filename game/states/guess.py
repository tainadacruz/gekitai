import pygame as pg

from game.data import GameData
from game.display import Display
from game.guess import Even, Odd
from game.state import State, Transition, TransitionType
from game.states.reveal import RevealState
from game.widgets import Button, Text


class GuessState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)
        self.__data = data

        self.__title = Text(
            pg.Rect(
                0,
                self.__display.resolution[1] // 2 - 50,
                self.__display.resolution[0],
                40,
            ),
            "Guesser, é par ou ímpar?",
            (255, 255, 255),
        )

        self.__even_button = Button(
            pg.Rect(
                self.__display.resolution[0] // 2 - 250,
                self.__display.resolution[1] // 2 + 50,
                100,
                40,
            ),
            "Par",
        )

        self.__odd_button = Button(
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
        self.__title.draw(self.__surface)
        self.__even_button.draw(self.__surface)
        self.__odd_button.draw(self.__surface)

    def execute(self):
        self.__display.draw(self.__surface)

        if self.__even_button.clicked():
            self.__data.round.guess = Even()
        elif self.__odd_button.clicked():
            self.__data.round.guess = Odd()

        if self.__data.round.guess is not None:
            return Transition(TransitionType.SWITCH, RevealState(self.__data))

        return Transition(TransitionType.NONE)
