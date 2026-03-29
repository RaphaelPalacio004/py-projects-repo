import math
from loguru import logger


class Factorial:
    def __init__(self, userinput, n, result):
        self.userinput = userinput
        self.n = n
        self.result = result

    def FactorialValue(self):
        try:
            self.userinput = int(input("Enter a factorial value: "))
            if self.userinput < 0:
                logger.warning(
                    "Negative integers cannot be calculated as a factorial value."
                )
            else:
                for index in reversed(range(0, self.userinput)):
                    self.n = math.factorial(index + 1) * 1
                    self.result = self.n
                    return self.result
        except ValueError:
            return logger.exception("The application encountered a value error.")

    def __str__(self):
        return f"{self.userinput} != {self.result}"


Result = Factorial(userinput=int, n=int, result=int)
Result.FactorialValue()
print(Result)
