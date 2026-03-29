from loguru import logger


class Palindrome:
    def __init__(self, userinput, origin, reversed_origin, is_palindrome):
        self.userinput = userinput
        self.origin = origin
        self.reversed_origin = reversed_origin
        self.is_palindrome = is_palindrome

    def GeneratePalindrome(self):
        try:
            self.userinput = str(input("Enter a keyword: "))
            while len(self.userinput) == 0:
                self.userinput = str(input("Enter a keyword: "))
            for letter in self.userinput:
                self.origin = letter[0 : len(self.userinput)]
            for rletter in reversed(self.userinput):
                self.reversed_origin = rletter[-1 : len(self.userinput)]

            self.is_palindrome = True if self.origin == self.reversed_origin else False

        except Exception:
            return logger.exception("The application encountered an error.")

    def __str__(self):
        if self.is_palindrome:
            return f"The keyword is a palindrome."
        else:
            return "The keyword is not a palindrome."


Result = Palindrome(userinput="", origin="", reversed_origin="", is_palindrome=False)
Result.GeneratePalindrome()
print(Result)
