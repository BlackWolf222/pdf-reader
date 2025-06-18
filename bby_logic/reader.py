import fitz

class PDFReader:
    """
    A class to read PDF files and extract text content.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self) -> str:
        """
        Reads a PDF file and returns its text content.

        Args:
            file_path (str): The path to the PDF file.

        Returns:
            str: The text content of the PDF file.
        """
        try:
            with fitz.open(self.file_path) as pdf:
                text = ""
                for page in pdf:
                    text += page.get_text()
                    print(text)
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return ""
