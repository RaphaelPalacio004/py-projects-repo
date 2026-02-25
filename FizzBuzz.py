def FizzBuzz():
    try:
        userInput = int(input("Enter a value in multiples of three, five, or both. : "))
        if userInput <= 0 or userInput >= 101:
            raise IndexError("Index is out of bounds.")
        isFizz = True if userInput % 3 == 0 else False
        isBuzz = True if userInput % 5 == 0 else False
        isFizzBuzz = True if userInput % 3 == 0 and userInput % 5 == 0 else False

        if isFizz == True and isFizzBuzz == False:
            print("Fizz")
        elif isBuzz == True and isFizzBuzz == False:
            print("Buzz")
        elif isFizzBuzz == True:
            print("FizzBuzz")
        else:
            print(
                f"The number value {userInput} does not correspond to multiples of three or five."
            )

        return isFizz, isBuzz, isFizzBuzz

    except ValueError as valExc:
        print(valExc)
    except Exception as exc:
        print(exc)


FizzBuzz()
