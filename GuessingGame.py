def GuessingGame():
    try:
        count = 1
        attempt = 3
        isGameOver = False
        guessName = "proxy"
        userInput = str(input("Enter the guess word: "))

        while userInput != guessName and count <= attempt and isGameOver == False:
            userInput = str(input("Enter the guess word: "))
            count += 1

        if userInput == guessName and count <= attempt:
            isGameOver = False
            print(
                f"Well done! You've figured out the word {guessName}. Tried attempt(s): {count}"
            )
        elif userInput != guessName and count > attempt:
            isGameOver = True
            print(
                f"You lose! You did not guess the word {guessName}; please try again. Tried attempt(s): {count}"
            )

    except Exception as exc:
        print(f"{exc}")


GuessingGame()
