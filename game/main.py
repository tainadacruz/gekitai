from game.display import Display
from game.input import Input
from game.mappings import mappings
from game.states.menu_state import MenuState
from game.states.state import Action


class Main:
    def __init__(self):
        self.__display = Display("Marbles", (800, 600), 30)
        self.__input = Input(mappings)
        self.__states = [MenuState()]

    def start(self):
        print("Starting game...")
        while True:
            self.__input.update()
            self.__display.tick()
            transition = self.__states[-1].execute()
            if transition.action == Action.POP:
                self.__states.pop()
            elif transition.action == Action.PUSH:
                self.__states.append(transition.state)
