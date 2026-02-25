import math


def Factorial():
    try:
        userInput = int(input("Enter a factorial value: "))
        if userInput < 0:
            raise ValueError(
                "Negative integers cannot be calculated as a factorial value."
            )
        else:
            for index in reversed(range(0, userInput)):
                n = math.factorial(index + 1) * 1
                result = n
                print(f"{userInput}! = {result}")
                return result
    except Exception as exc:
        print(exc)


Factorial()
