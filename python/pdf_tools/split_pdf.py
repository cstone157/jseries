import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(pdf_file_path, output_dir=None):
    """Splits a PDF file into individual pages and saves them as separate PDF files.

    Args:
        pdf_file_path: The path to the input PDF file.
        output_dir: The directory to save the split PDF files.
                    If None, defaults to the same directory as the input file.
    """

    try:
        reader = PdfReader(pdf_file_path)
        num_pages = len(reader.pages)

        if not output_dir:
            output_dir = os.path.dirname(pdf_file_path)  # Use the same directory if not specified

        base_filename = os.path.splitext(os.path.basename(pdf_file_path))[0]

        for i in range(num_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])

            output_filename = os.path.join(output_dir, f"{base_filename}_page_{i+1}.pdf")
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)

        print(f"PDF '{pdf_file_path}' split into {num_pages} pages and saved to '{output_dir}'.")

    except FileNotFoundError:
        print(f"Error: File '{pdf_file_path}' not found.")
    except Exception as e:  # Catch other potential errors (e.g., invalid PDF format)
        print(f"An error occurred: {e}")

# Example usage:
pdf_file = "./MIL-STD-6016G.pdf"  # Replace with the actual file name/path
split_pdf(pdf_file, output_dir="split_pdfs") # splits pdf and stores output in split_pdfs folder (will create it if it doesn't exist)

# OR to save in the same directory as the input PDF:
split_pdf(pdf_file)