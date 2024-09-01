from pathlib import Path


"""The first segment handles files system"""


class Filesystem:
    def __init__(self, filename: str) -> None:
        self.filename = Path(filename)

    # file not found
    def check_file_not_found(self) -> bool:
        if not self.filename.exists():
            raise FileNotFoundError(f"The file{self.filename} does not exists")
        return True

    # file already exists
    def check_file_already_exists(self) -> bool:
        if self.filename.exists():
            raise FileExistsError(f"The file {self.filename}already exists")
        return True

    # checking file or not
    def check_file_or_directory(self):
        if not self.filename.is_file():
            raise IsADirectoryError(f"{self.filename}is a directory and not a file")
        return True

    # reading files
    def read_file(self) -> str:
        try:
            self.check_file_or_directory()
            with open(self.filename, "r") as file:
                content = file.read()

        except PermissionError:
            raise PermissionError(f"Permission denied to the file {self.filename}")

        except Exception as e:
            raise RuntimeError(f"An unexpected error occured {e}")

        return content


if __name__ == "__main__":
    filesystem = Filesystem("/path/to/file.pdf")
    filesystem.check_file_or_directory()
    filesystem.check_file_not_found()
    filesystem.read_file()
