import pygame as pg
from game.data import GameData

from game.display import Display
from game.input import Input
from game.states.state import Action, State, Transition
from game.widgets import Button, TextBox
from game.player import Player


class GameState(State):
    def __init__(self) -> None:
        self.__data = GameData(Player("PlayerA"), Player("PlayerB"))
        self.__states = [HideState(self.__data)]

    def execute(self):
        transition = self.__states[-1].execute()
        if transition.action == Action.SWITCH:
            self.__states[-1] = transition.state
        return Transition(Action.NONE)


class HideState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)

        self.__data = data

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

    def execute(self):
        self.__text_box.update(self.__surface)

        if self.__submit.clicked():
            try:
                amount = int(self.__text_box.text)
                if self.__data.hider.can_hide(amount):
                    self.__data.round.hidden = amount
                    return Transition(Action.SWITCH, BetState(self.__data))
            except ValueError:
                self.__text_box.clear(self.__surface)

        self.__display.draw(self.__surface)
        return Transition(Action.NONE)


class BetState(State):
    def __init__(self, data: GameData) -> None:
        self.__display = Display()
        self.__surface = pg.Surface(self.__display.resolution)
        self.__data = data
        self.__draw_ui()

    def __draw_ui(self):
        pg.draw.rect(self.__surface, (0, 0, 255), self.__surface.get_rect())

    def execute(self):
        self.__display.draw(self.__surface)
        return Transition(Action.NONE)
