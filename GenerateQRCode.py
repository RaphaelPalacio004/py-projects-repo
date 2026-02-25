import qrcode
import os
import validators
import time


def GenerateQRCode():
    try:
        userInput = str(input("Enter a website url: "))
        validateUrl = True if validators.url(userInput) else False
        while len(userInput) < 1 or validateUrl == False:
            print("The provided URL is invalid or the input value is left empty.")
            userInput = str(input("Enter a website url: "))
        parentDirectory = r"C:\Users\Admin\Desktop\Py Projects"
        childFolder = "Generated QR"
        mergePath = os.path.join(parentDirectory, childFolder)
        isPathExisting = True if os.path.exists(mergePath) else False
        if isPathExisting:
            os.chdir(mergePath)
            generate = qrcode.make(userInput)
            newFile = str(input("Save file as: "))
            concat = os.path.join(newFile + "." + "jpeg")
            for qr_file in mergePath:
                if os.path.isfile(concat):
                    raise FileExistsError("File already exist.")
            time.sleep(1.5)
            generate.save(concat, format="JPEG")
            print(f"File successfully saved as: {concat}")
            return generate
    except Exception as exc:
        print(exc)


GenerateQRCode()
