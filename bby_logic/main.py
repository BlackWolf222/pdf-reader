from reader import PDFReader
from speaker import Speaker

def main():
    pdf_file_path = "abizt01.pdf"

    pdf_reader = PDFReader(pdf_file_path)

    pdf_text = pdf_reader.read_pdf()
    if pdf_text:
        speaker = Speaker(text=pdf_text)
        
        speaker.text_to_speech()
    else:
        print("No text extracted from the PDF file.")

if __name__ == "__main__":
    main()