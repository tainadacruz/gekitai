import pygame as pg

from game.utils import Singleton, end


class Mouse:
    def __init__(self) -> None:
        self.__position = (0, 0)
        self.__pressed = False

    @property
    def position(self) -> tuple[int, int]:
        return self.__position

    @property
    def pressed(self) -> bool:
        return self.__pressed

    def update(self):
        self.__position = pg.mouse.get_pos()
        self.__pressed = pg.mouse.get_pressed()[0]


class Input(metaclass=Singleton):
    def __init__(self, mappings: dict[int, str] = None):
        self.__mappings = mappings if mappings else {}
        self.__pressed = set()
        self.__just_pressed = set()
        self.__mouse = Mouse()

    @property
    def pressed(self) -> set[str]:
        return self.__pressed

    @property
    def just_pressed(self) -> set[str]:
        return self.__just_pressed

    @property
    def mouse(self) -> Mouse:
        return self.__mouse

    def update(self):
        """Atualiza as teclas"""
        self.__just_pressed.clear()
        self.__mouse.update()

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
