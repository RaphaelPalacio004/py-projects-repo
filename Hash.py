import hashlib
import getpass


def Hash():
    try:
        userInput = getpass.getpass(prompt="Enter a keyword: ", echo_char="*")
        while len(userInput) == 0:
            userInput = getpass.getpass(prompt="Enter a keyword: ", echo_char="*")
        encodedMessage = userInput.encode("utf-8")
        hashCode = hashlib.sha256(encodedMessage)
        for negative_value in userInput:
            if userInput < str(0) or negative_value.startswith("-"):
                raise ValueError(
                    f"A negative symbol or integer(s) is detected: {userInput}"
                )
        if len(userInput) > 20:
            raise IndexError(
                f"Index out of bounds!, total length value: {len(userInput)}, exceeded the length value of (20)"
            )
        result = hashCode.hexdigest()
        print(f"Hash code: {result}")
        return result
    except Exception as exc:
        print(exc)


Hash()
