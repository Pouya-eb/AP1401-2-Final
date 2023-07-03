import asyncio


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


async def find_root_binary_search(equation, left, right, precision):
    
    while True:
        middle = (left + right) / 2
        if ((middle - left) < precision or (right - middle) < precision):
            print(middle)
            return middle

        await asyncio.sleep(0.01)
        if (equation.compute(middle) > 0):
            print("Computing")
            right = middle
        else:
            left = middle

