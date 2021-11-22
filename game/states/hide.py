import pygame as pg

from game.data import GameData
from game.display import Display
from game.states.bet import BetState
from game.state import State, Transition, TransitionType
from game.widgets import Button, Text, TextBox


class HideState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)

        self.__data = data

        self.__text = Text(
            pg.Rect(
                self.__display.resolution[0] // 2 - 200,
                self.__display.resolution[1] // 2 - 50,
                400,
                40,
            ),
            "Hider, esconda um número.",
            (255, 255, 255),
        )

        self.__text_box = TextBox(
            pg.Rect(
                self.__display.resolution[0] // 2 - 200,
                self.__display.resolution[1] // 2,
                400,
                40,
            )
        )
        self.__submit = Button(
            pg.Rect(
                self.__display.resolution[0] // 2 - 200,
                self.__display.resolution[1] // 2 + 50,
                400,
                40,
            ),
            "Esconder",
        )

        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(self.__surface, (0, 0, 0), self.__surface.get_rect())
        self.__text_box.draw(self.__surface)
        self.__submit.draw(self.__surface)
        self.__text.draw(self.__surface)

    def execute(self):
        self.__text_box.update(self.__surface)

        if self.__submit.clicked():
            try:
                amount = int(self.__text_box.text)
                if self.__data.hider.can_hide(amount):
                    self.__data.round.hidden = amount
                    return Transition(
                        TransitionType.SWITCH, BetState(self.__data)
                    )
                else:
                    self.__text_box.clear(self.__surface)
            except ValueError:
                self.__text_box.clear(self.__surface)

        self.__display.draw(self.__surface)
        return Transition(TransitionType.NONE)
