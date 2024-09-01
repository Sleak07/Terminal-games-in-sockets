""" this section defines the pdf checks and storing chunks
        to it and APi endpoints are defined"""

from pypdf import PdfReader
from pathlib import Path
import filesystem


class Extractor:
    def __init__(self, filename) -> None:
        self.filename = Path(filename)
        self.filesystem = filesystem.Filesystem(filename)

    """This segment checks all the filesystem function previously defined"""

    def get_chunks(self) -> str:  # type: ignore
        if self.filesystem.check_file_or_directory():
            if self.filesystem.check_file_not_found:
                pdf = PdfReader(self.filename)

                chunks = []
                for pdf in pdf.pages:
                    chunks.append(pdf.extract_text())

                return "/n".join(chunks)

        else:
            raise FileNotFoundError(f"File '{self.filename}' not found.")


if __name__ == "main":
    extractor = Extractor("/path/pdf")
    chunks = extractor.get_chunks()
    print(chunks)


# breaking the pdf into chunks
