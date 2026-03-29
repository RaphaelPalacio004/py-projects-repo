import os
import random
from loguru import logger


class Rename:
    def __init__(
        self,
        file_extension,
        random_file_extension,
        parent,
        child,
        merge_directory,
        is_existing,
        userinput,
        converted_value,
        item_file,
        rename_file,
        result,
    ):
        self.file_extension = file_extension
        self.random_file_extension = random_file_extension
        self.parent = parent
        self.child = child
        self.merge_directory = merge_directory
        self.is_existing = is_existing
        self.userinput = userinput
        self.converted_value = converted_value
        self.item_file = item_file
        self.rename_file = rename_file
        self.result = result

    def FileRename(self):
        try:
            self.file_extension = [
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
            self.random_file_extension = random.choice(self.file_extension)
            self.parent = r"C:\Users\Admin\Desktop\Py Projects"
            self.child = "SubFolder"
            self.merge_directory = os.path.join(self.parent, self.child)
            self.is_existing = True if os.path.exists(self.merge_directory) else False
            if self.is_existing:
                os.chdir(self.merge_directory)
                self.userinput = str(input("Select an index value: "))
                self.converted_value = int(self.userinput)
            for index, self.item_file in enumerate(os.listdir(self.merge_directory)):
                if self.converted_value == index:
                    self.rename_file = str(input("Rename the selected file to: "))
                    self.result = os.rename(
                        self.item_file,
                        self.rename_file + "." + self.random_file_extension,
                    )
                    break
        except ValueError:
            return logger.exception("The application encountered a value error.")
        except TypeError:
            return logger.exception("The application encountered a type error.")
        except FileNotFoundError:
            return logger.exception("The application encountered a file not found error.")

    def __str__(self):
        return f"Previous file name: {self.item_file}, Current file name: {self.rename_file} with the file extension of .{self.random_file_extension}"


Result = Rename(
    file_extension="",
    random_file_extension="",
    parent="",
    child="",
    merge_directory="",
    is_existing=False,
    userinput="",
    converted_value=int,
    item_file="",
    rename_file="",
    result="",
)
Result.FileRename()
print(Result)
