import random


def RockPaperScissors():
    try:
        selection = ["rock", "paper", "scissors"]
        computer = random.choices(selection)
        for selected_item in computer:
            result = selected_item.strip("' '")
        userInput = str(input("Enter an option (rock, paper, scissors): ")).lower()
        while len(userInput) < 1:
            print("The input value is left empty, please try again.")
            userInput = str(input("Enter an option (rock, paper, scissors): ")).lower()
        if userInput != "rock" and userInput != "paper" and userInput != "scissors" and userInput != " ":
            raise ValueError("Incorrect value type is provided.")
        match userInput:
            case "rock":
                if userInput == "rock" and result == "rock":
                    print(f"Human: {userInput} Vs. Computer: {result}, It's a DRAW!")
                elif userInput == "rock" and result == "paper":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Rock loses against to Paper!"
                    )
                elif userInput == "rock" and result == "scissors":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Rock beats Scissors!"
                    )
            case "paper":
                if userInput == "paper" and result == "paper":
                    print(f"Human: {userInput} Vs. Computer: {result}, It's a DRAW!")
                elif userInput == "paper" and result == "rock":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Paper beats Rock!"
                    )
                elif userInput == "paper" and result == "scissors":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Paper loses against to Scissors!"
                    )
            case "scissors":
                if userInput == "scissors" and result == "scissors":
                    print(f"Human: {userInput} Vs. Computer: {result}, It's a DRAW!")
                elif userInput == "scissors" and result == "rock":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Scissors loses against to Rock!"
                    )
                elif userInput == "scissors" and result == "paper":
                    print(
                        f"Human: {userInput} Vs. Computer: {result}, Scissors beats Paper!"
                    )
        return userInput, result
    except Exception as exc:
        print(f"{exc}")


RockPaperScissors()
