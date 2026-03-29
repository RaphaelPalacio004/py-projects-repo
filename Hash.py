import getpass
import hashlib
from loguru import logger


class Hashing:
    def __init__(self, userinput, encoded_message, hash_object, result):
        self.userinput = userinput
        self.encoded_message = encoded_message
        self.hash_object = hash_object
        self.result = result

    def GenerateHash(self):
        try:
            self.userinput = getpass.getpass(prompt="Enter a keyword: ", echo_char="*")

            while len(self.userinput) == 0:
                self.userinput = getpass.getpass(
                    prompt="Enter a keyword: ", echo_char="*"
                )

            self.encoded_message = self.userinput.encode("utf-8")
            self.hash_object = hashlib.sha256(self.encoded_message)
            self.result = self.hash_object.hexdigest()
        except Exception:
            return logger.exception("The application encountered an error")

    def __str__(self):
        return f"Hash code: {self.result}"


Result = Hashing(userinput="", encoded_message="", hash_object=hash, result="")
Result.GenerateHash()
print(Result)
