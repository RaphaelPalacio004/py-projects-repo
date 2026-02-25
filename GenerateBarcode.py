from barcode import UPCA
import time
import os


def GenerateBarcode():
    try:
        parentDirectory = r"C:\Users\Admin\Desktop\Py Projects"
        childFolder = "Generated Barcode"
        mergePath = os.path.join(parentDirectory, childFolder)
        isPathExisting = True if os.path.exists(mergePath) else False
        if isPathExisting:
            os.chdir(mergePath)
            userInput = str(input("Enter a numerical value: "))
            while len(userInput) < 1:
                print("The input value is left empty, please try again.")
                userInput = str(input("Enter a numerical value: "))
            if len(userInput) > 12:
                raise IndexError(
                    f"UPC-A consists of only 12 digits, digits provided: {len(userInput)}"
                )
            generate = UPCA(userInput)
            newFile = str(input("Save file as: "))
            concat = os.path.join(newFile + "." + "svg")
            for barcode_file in mergePath:
                if os.path.isfile(concat):
                    raise FileExistsError("File already exist.")

            time.sleep(1.5)
            barcode = generate.save(newFile)
            print(
                f"File successfully saved as: {concat} with the generated barcode number of: {generate}"
            )
            return barcode
    except Exception as exc:
        print(f"{exc}")


GenerateBarcode()
