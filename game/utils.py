import sys
import pygame as pg


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def end():
    """Finaliza o pygame e encerra o processo"""
    pg.quit()
    sys.exit()
