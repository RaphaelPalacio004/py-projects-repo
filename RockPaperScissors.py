import random
from loguru import logger


class RockPaperScissors:
    def __init__(self, selection, computer, result, user_input):
        self.selection = selection
        self.computer = computer
        self.result = result
        self.user_input = user_input

    def RockPaperShoot(self):
        try:
            self.selection = ["rock", "paper", "scissors"]
            self.computer = random.choices(self.selection)
            for selected_item in self.computer:
                self.result = selected_item.strip("' '")
            self.user_input = str(
                input("Enter an option (rock, paper, scissors): ")
            ).lower()
            while len(self.user_input) < 1:
                logger.warning("The input value is left empty, please try again.")
                self.user_input = str(
                    input("Enter an option (rock, paper, scissors): ")
                ).lower()
        except Exception:
            return logger.exception("The application encountered an error.")

    def __str__(self):
        if (
            self.user_input != "rock"
            and self.user_input != "paper"
            and self.user_input != "scissors"
            and self.user_input != " "
        ):
            logger.warning("Incorrect value type is provided.")
        match self.user_input:
            case "rock":
                if self.user_input == "rock" and self.result == "rock":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, It's a DRAW!"

                elif self.user_input == "rock" and self.result == "paper":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Rock loses against to Paper!"

                elif self.user_input == "rock" and self.result == "scissors":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Rock beats Scissors!"
            case "paper":
                if self.user_input == "paper" and self.result == "paper":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, It's a DRAW!"

                elif self.user_input == "paper" and self.result == "rock":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Paper beats Rock!"

                elif self.user_input == "paper" and self.result == "scissors":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Paper loses against to Scissors!"

            case "scissors":
                if self.user_input == "scissors" and self.result == "scissors":
                    return "Human: {self.user_input} Vs. Computer: {self.result}, It's a DRAW!"
                elif self.user_input == "scissors" and self.result == "rock":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Scissors loses against to Rock!"

                elif self.user_input == "scissors" and self.result == "paper":
                    return f"Human: {self.user_input} Vs. Computer: {self.result}, Scissors beats Paper!"


Result = RockPaperScissors(selection="", computer="", result="", user_input="")
Result.RockPaperShoot()
print(Result)
