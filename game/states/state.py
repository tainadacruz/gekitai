from abc import ABC, abstractmethod
from enum import Enum, auto


class State(ABC):
    @abstractmethod
    def execute(self):
        """Lógica de execução do estado"""


class Action(Enum):
    NONE = auto()
    PUSH = auto()
    POP = auto()
    SWITCH = auto()


class Transition:
    def __init__(self, action: Action = Action.NONE, state: State = None):
        self.__action = action
        self.__state = state

    @property
    def action(self) -> Action:
        return self.__action

    @property
    def state(self) -> State:
        return self.__state
