from game.display import Display
from game.input import Input
from game.mappings import mappings
from game.state import StateMachine
from game.states.menu import MenuState


class Main:
    def __init__(self):
        self.__display = Display("Marbles", (800, 600), 30)
        self.__input = Input(mappings)
        self.__state = StateMachine(MenuState())

    def start(self):
        print("Starting game...")
        while True:
            self.__input.update()
            self.__display.tick()
            self.__state.execute()
