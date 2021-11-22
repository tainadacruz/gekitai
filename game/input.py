import pygame as pg

from game.utils import Singleton, end


class Input(metaclass=Singleton):
    def __init__(self, mappings: dict[int, str] = None):
        self.__mappings = mappings if mappings else {}
        self.__pressed = set()
        self.__just_pressed = set()
        self.__mouse_position = (0, 0)
        self.__mouse = None

    @property
    def pressed(self) -> set[str]:
        return self.__pressed

    @property
    def just_pressed(self) -> set[str]:
        return self.__just_pressed

    @property
    def mouse(self) -> int:
        return self.__mouse

    @property
    def mouse_position(self) -> tuple[int, int]:
        return self.__mouse_position

    def update(self):
        """Atualiza as teclas"""
        self.__just_pressed.clear()
        self.__mouse = None

        self.__mouse_position = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            elif (
                event.type in [pg.KEYDOWN, pg.KEYUP]
                and event.key in self.__mappings
            ):
                action = self.__mappings[event.key]
                if event.type == pg.KEYDOWN:
                    self.__pressed.add(action)
                    self.__just_pressed.add(action)
                elif event.type == pg.KEYUP:
                    self.__pressed.remove(action)
            elif event.type in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP]:
                self.__mouse = event.type
