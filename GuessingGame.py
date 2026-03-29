from loguru import logger

class Guess:
    def __init__(self, count, attempt, is_gameover, guess_name, userinput):
        self.count = count
        self.attempt = attempt
        self.is_gameover = is_gameover
        self.guess_name = guess_name
        self.userinput = userinput

    def GuessingGame(self):
        try:
            self.count = 1
            self.attempt = 3
            self.is_gameover = False
            self.guess_name = "proxy"
            self.userinput = str(input("Enter the guess word: "))

            while (
                self.userinput != self.guess_name
                and self.count <= self.attempt
                and self.is_gameover == False
            ):
                self.userinput = str(input("Enter the guess word: "))
                self.count += 1
        except Exception:
            return logger.exception("The application encountered an error.")

    def __str__(self):
        if self.userinput == self.guess_name and self.count <= self.attempt:
            self.is_gameover = False
            return f"Well done! You've figured out the word {self.guess_name}. Tried attempt(s): {self.count}"
        elif self.userinput != self.guess_name and self.count > self.attempt:
            self.is_gameover = True
            return f"You lose! You did not guess the word {self.guess_name}; please try again. Tried attempt(s): {self.count}"


Result = Guess(count=int, attempt=int, is_gameover=False, guess_name="", userinput="")
Result.GuessingGame()
print(Result)
