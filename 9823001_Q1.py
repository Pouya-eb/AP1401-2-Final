class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self, x):
        return self.a * x + self.b


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def compute(self, x):
        return self.a * x ** 2 + self.b * x + self.c

