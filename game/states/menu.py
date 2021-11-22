import pygame as pg

from game.display import Display
from game.state import State, Transition, TransitionType
from game.states.hide import HideState
from game.utils import end
from game.widgets import Button


class MenuState(State):
    def __init__(self) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)

        self.__start_button = Button(
            pg.Rect(
                10,
                self.__display.resolution[1] // 2,
                self.__display.resolution[0] // 2,
                80,
            ),
            "START",
        )
        self.__exit_button = Button(
            pg.Rect(
                10,
                self.__display.resolution[1] // 2 + 90,
                self.__display.resolution[0] // 2,
                80,
            ),
            "QUIT",
        )

        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(self.__surface, (255, 255, 255), self.__surface.get_rect())
        self.__start_button.draw(self.__surface)
        self.__exit_button.draw(self.__surface)

    def execute(self) -> Transition:
        self.__display.draw(self.__surface)
        if self.__start_button.clicked():
            return Transition(TransitionType.PUSH, HideState())
        elif self.__exit_button.clicked():
            end()
        return Transition(TransitionType.NONE)
