import pygame as pg

from game.data import GameData
from game.display import Display
from game.state import State, Transition, TransitionType
from game.widgets import Text


class RevealState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)
        self.__data = data

        self.__correct = data.execute()

        self.__text = Text(
            pg.Rect(
                0,
                self.__display.resolution[1] // 2 - 50,
                self.__display.resolution[0],
                40,
            ),
            f"{self.__data.guesser.name} acertou e ganhou a rodada"
            if self.__correct
            else f"{self.__data.guesser.name} errou, {self.__data.hider.name} ganhou a rodada",
            (255, 255, 255),
        )

        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(
            self.__surface,
            (3, 122, 118) if self.__correct else (244, 71, 134),
            self.__surface.get_rect(),
        )
        self.__text.draw(self.__surface)

    def execute(self):
        self.__display.draw(self.__surface)
        return Transition(TransitionType.NONE)
