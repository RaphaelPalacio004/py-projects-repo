def Palindrome():
    try:
        userInput = str(input("Enter a keyword: "))
        while len(userInput) == 0:
            userInput = str(input("Enter a keyword: "))
        for letter in userInput:
            origin = letter[0 : len(userInput)]
        for rletter in reversed(userInput):
            reversedOrigin = rletter[-1 : len(userInput)]
        isPalindrome = True if origin == reversedOrigin else False
        if isPalindrome:
            print(f"The keyword is a palindrome.")
        else:
            print("The keyword is not a palindrome.")
        return origin, reversedOrigin
    except Exception as exc:
        print(exc)


Palindrome()
