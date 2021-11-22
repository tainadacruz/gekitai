import pygame as pg
from game.data import GameData

from game.display import Display
from game.player import Player
from game.state import State, Transition, TransitionType
from game.states.hide import HideState
from game.utils import end
from game.widgets import Button


class MenuState(State):
    def __init__(self) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)

        self.__logo = pg.image.load("./img/logo.png")
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
        pg.draw.rect(self.__surface, (0, 0, 0), self.__surface.get_rect())
        self.__surface.blit(self.__logo, (10, 150))
        self.__start_button.draw(self.__surface)
        self.__exit_button.draw(self.__surface)

    def execute(self) -> Transition:
        self.__display.draw(self.__surface)
        if self.__start_button.clicked():
            return Transition(
                TransitionType.PUSH,
                HideState(
                    GameData(Player("Player A"), Player("Player B"))
                ),  # Isso deve ser mudado no futuro
            )
        elif self.__exit_button.clicked():
            end()
        return Transition(TransitionType.NONE)
