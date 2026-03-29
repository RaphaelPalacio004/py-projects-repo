import qrcode
import os
import validators
import time
from loguru import logger


class QRCode:

    def __init__(
        self,
        user_input,
        is_url,
        parent,
        child,
        merge_directory,
        is_existing,
        generate,
        new_file,
        concatenate,
    ):
        self.user_input = user_input
        self.is_url = is_url
        self.parent = parent
        self.child = child
        self.merge_directory = merge_directory
        self.is_existing = is_existing
        self.generate = generate
        self.new_file = new_file
        self.concatenate = concatenate

    def GenerateQRCode(self):
        try:
            self.user_input = str(input("Enter a website url: "))
            self.is_url = True if validators.url(self.user_input) else False
            while len(self.user_input) < 1 or self.is_url == False:
                print("The provided URL is invalid or the input value is left empty.")
                self.user_input = str(input("Enter a website url: "))

            self.parent = r"C:\Users\Admin\Desktop\Py Projects"
            self.child = "Generated QR"
            self.merge_directory = os.path.join(self.parent, self.child)
            self.is_existing = True if os.path.exists(self.merge_directory) else False
        except FileNotFoundError:
            return logger.exception("The application encountered a file not found error.")
        except Exception:
            return logger.exception("The application encountered an error.")

    def __str__(self):
        if self.is_existing:
            os.chdir(self.merge_directory)
            self.generate = qrcode.make(self.user_input)
            self.new_file = str(input("Save file as: "))
            self.concatenate = os.path.join(self.new_file + "." + "jpeg")
            for qr_file in self.merge_directory:
                if os.path.isfile(self.concatenate):
                    raise FileExistsError("File already exist.")
            time.sleep(1.5)
            self.generate.save(self.concatenate, format="JPEG")
            return f"File successfully saved as: {self.concatenate}"


Result = QRCode(
    user_input="",
    is_url=False,
    parent="",
    child="",
    merge_directory="",
    is_existing=False,
    generate="",
    new_file="",
    concatenate="",
)
Result.GenerateQRCode()
print(Result)
