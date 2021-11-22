import pygame as pg

from game.input import Input


class Button:
    def __init__(self, rect: pg.Rect, text=""):
        self.__rect = rect
        self.__text = Text(rect, text)

    def draw(self, surface: pg.Surface) -> None:
        pg.draw.rect(surface, (0, 155, 0), self.__rect)
        self.__text.draw(surface)

    def clicked(self) -> bool:
        return Input().mouse.pressed and self.__rect.collidepoint(
            Input().mouse.position
        )


class TextBox:
    def __init__(self, rect: pg.Rect):
        self.__rect = rect
        self.__text = ""
        self.__font = pg.font.Font(None, 32)

    @property
    def text(self) -> str:
        return self.__text

    def clear(self, surface: pg.Surface) -> None:
        self.__text = ""
        self.draw(surface)

    def draw(self, surface: pg.Surface) -> None:
        pg.draw.rect(surface, (155, 155, 155), self.__rect)
        text = self.__font.render(self.__text, False, (0, 0, 0))
        surface.blit(text, self.__rect)

    def update(self, surface: pg.Surface) -> None:
        text = self.__text
        if "backspace" in Input().just_pressed:
            self.__text = self.__text[:-1]
        else:
            for key in Input().just_pressed:
                if len(key) == 1:
                    self.__text += key
        if text != self.__text:
            self.draw(surface)


class Text:
    def __init__(
        self, rect: pg.Rect, text: str, color: tuple[int, int, int] = (0, 0, 0)
    ):
        self.__rect = rect
        self.__font = pg.font.Font(None, 32)
        self.__text = text
        self.__color = color

    def draw(self, surface: pg.Surface) -> None:
        text = self.__font.render(self.__text, False, self.__color)
        surface.blit(text, self.__rect)
