import pygame as pg

from game.utils import Singleton


class Display(metaclass=Singleton):
    def __init__(
        self,
        title: str = "",
        resolution: tuple[int, int] = (800, 600),
        framerate: int = 60,
    ):
        pg.init()
        pg.font.init()
        pg.display.set_caption(title)

        self.__framerate = framerate
        self.__clock = pg.time.Clock()
        self.__window = pg.display.set_mode(
            resolution,
            pg.RESIZABLE | pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED,
            32,
        )
        self.tick()

    @property
    def resolution(self) -> tuple[int, int]:
        return self.__window.get_size()

    def tick(self) -> float:
        """Atualiza o clock do jogo"""
        return self.__clock.tick(self.__framerate) * 0.001

    def draw(self, surface: pg.Surface):
        """Desenha uma superfície na janela"""
        self.__window.fill((0, 0, 0))
        self.__window.blit(surface, (0, 0))
        pg.display.update()
