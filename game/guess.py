from abc import ABC, abstractmethod


class Guess(ABC):
    @abstractmethod
    def execute(self, number: str) -> bool:
        pass


class Even(Guess):
    def execute(self, number: str) -> bool:
        return (number % 2) == 0


class Odd(Guess):
    def execute(self, number: str) -> bool:
        return (number % 2) != 0
