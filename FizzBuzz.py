from loguru import logger


class FizzBuzz:
    def __init__(self, userinput, is_fizz, is_buzz, is_fizzbuzz):
        self.userinput = userinput
        self.is_fizz = is_fizz
        self.is_buzz = is_buzz
        self.is_fizzbuzz = is_fizzbuzz

    def ValidateFizzBuzz(self):
        try:
            self.userinput = int(
                input("Enter a value in multiples of three, five, or both. : ")
            )
            self.is_fizz = True if self.userinput % 3 == 0 else False
            self.is_buzz = True if self.userinput % 5 == 0 else False
            self.is_fizzbuzz = (
                True if self.userinput % 3 == 0 and self.userinput % 5 == 0 else False
            )
            if self.is_fizz == False and self.is_buzz == False:
                return logger.warning(
                    "The value does not correlate to either the multiple of three or five."
                )
        except ValueError:
            return logger.exception("The application encountered a value error.")

    def __str__(self):
        if self.is_fizz == True and self.is_fizzbuzz == False:
            return f"FIZZ"
        elif self.is_buzz == True and self.is_fizzbuzz == False:
            return f"BUZZ"
        elif self.is_fizzbuzz == True:
            return f"FIZZBUZZ"


Result = FizzBuzz(userinput=int, is_fizz=False, is_buzz=False, is_fizzbuzz=False)
Result.ValidateFizzBuzz()
print(Result)
