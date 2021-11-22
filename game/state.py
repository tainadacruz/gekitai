from abc import ABC, abstractmethod
from enum import Enum, auto


class State(ABC):
    @abstractmethod
    def execute(self) -> "Transition":
        """Lógica de execução do estado"""


class TransitionType(Enum):
    NONE = auto()
    PUSH = auto()
    POP = auto()
    SWITCH = auto()


class Transition:
    def __init__(
        self, type: TransitionType = TransitionType.NONE, state: State = None
    ):
        self.__type = type
        self.__state = state

    @property
    def type(self) -> TransitionType:
        return self.__type

    @property
    def state(self) -> State:
        return self.__state


class StateMachine:
    def __init__(self, initial: State) -> None:
        self.__states = [initial]

    def execute(self) -> None:
        self.__change(self.__states[-1].execute())

    def __change(self, transition: Transition) -> None:
        if transition.type == TransitionType.PUSH:
            self.__states.append(transition.state)
        elif transition.type == TransitionType.POP:
            self.__states.pop()
        elif transition.type == TransitionType.SWITCH:
            self.__states.pop()
            self.__states.append(transition.state)
