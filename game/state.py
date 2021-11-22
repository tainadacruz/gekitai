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
        self, action: TransitionType = TransitionType.NONE, state: State = None
    ):
        self.__action = action
        self.__state = state

    @property
    def action(self) -> TransitionType:
        return self.__action

    @property
    def state(self) -> State:
        return self.__state


class StateMachine:
    def __init__(self) -> None:
        self.__states: list[State] = []

    def execute(self) -> None:
        self.__change(self.states[-1].execute())

    def __change(self, transition: Transition) -> None:
        if transition.type == TransitionType.PUSH:
            self.__states.append(transition.state)
        elif transition.type == TransitionType.POP:
            self.__states.pop()
        elif transition.type == TransitionType.CHANGE:
            self.__states.pop()
            self.__states.append(transition.state)
