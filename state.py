class State():
    def __init__(self):
        self.odd = False
        self.even = False

    def execute(self, number):
        number = int(number)
        if (number % 2 == 0):
            even = True
        else:
            odd = True