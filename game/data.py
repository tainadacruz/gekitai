from game.guess import Guess
from game.player import Player


class RoundData:
    def __init__(self):
        self.hidden: int = None
        self.bet: int = None
        self.guess: Guess = None

    def reset(self):
        self.hidden = None
        self.bet = None
        self.guess = None

    def execute(self, hider: Player, guesser: Player):
        if self.hidden == None or self.bet == None or self.guess == None:
            raise AttributeError()
        guess_correct = self.guess.execute(self.hidden)
        if guess_correct:
            guesser.win(self.bet)
        else:
            hider.win(self.bet)


class GameData:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.__hider = player1
        self.__guesser = player2
        self.__round = RoundData()

    @property
    def hider(self) -> Player:
        return self.__hider

    @property
    def guesser(self) -> Player:
        return self.__guesser

    @property
    def round(self) -> RoundData:
        return self.__round

    def switch(self) -> None:
        self.__hider, self.__guesser = self.__guesser, self.__hider
        self.__round.reset()
