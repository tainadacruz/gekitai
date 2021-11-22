from game.guess import Guess


class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__marbles = 10

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def guess(self) -> Guess:
        """Fazer lógica, retornar Even ou Odd"""

    def can_bet(self, n: int) -> bool:
        return 0 < n <= self.__marbles

    def can_hide(self, n: int) -> bool:
        return 0 <= n <= self.__marbles

    def win(self, marbles: int):
        self.__marbles += marbles

    def lose(self, marbles: int):
        self.__marbles -= marbles
