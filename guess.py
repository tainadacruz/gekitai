from state import State

class Guess():
    def __init__(self, state):
        self.state = state

    def execute(self, number):
        number = int(number)

        if (self.state.even) and (number % 2 == 0):
            return True
        elif (self.state.odd) and (number % 2 != 0):
            return True
        else:
            return False

    def state(self, input):
        self.state = input
        


