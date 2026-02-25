import os
import random


def FileRename():
    try:
        fileExtensions = [
            "txt",
            "exe",
            "bat",
            "jpeg",
            "png",
            "gif",
            "psd",
            "pdf",
            "docx",
            "csv",
            "mp3",
            "html",
            "zip",
            "svg",
            "wav",
            "xml",
        ]
        randomFileExtensions = random.choice(fileExtensions)
        parentDirectory = r"C:\Users\Admin\Documents"
        childFolder = "SubFolder"
        mergePath = os.path.join(parentDirectory, childFolder)
        isPathExisting = True if os.path.exists(mergePath) else False
        if isPathExisting:
            os.chdir(mergePath)
            userInput = str(input("Select an index value: "))
            convertedValue = int(userInput)
            for index, itemFile in enumerate(os.listdir(mergePath)):
                if convertedValue == index:
                    renameFile = str(input("Rename the selected file to: "))
                    result = os.rename(
                        itemFile, renameFile + "." + randomFileExtensions
                    )
                    print(
                        f"Previous file name: {itemFile}, Current file name: {renameFile} with the file extension of {randomFileExtensions}"
                    )
                    break
            return result
    except Exception as exc:
        print(exc)


FileRename()
