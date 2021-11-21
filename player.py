from pygame import Rect

class Player(Rect):
    def __init__(self, name, marbles, left, top):
        self.name = name
        self.marbles = marbles
        self.rect = Rect(left, top, 50, 50)
    
    def bet(self, input):
        return input

    def hide(self, input):
        return input

    def win( self, marbles):
        self.marbles += marbles

    def lose(self, marbles):
        self.marbles -= marbles