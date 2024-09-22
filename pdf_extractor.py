import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extract text from the provided PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

if __name__ == "__main__":
    # Test the function
    pdf_path = "fecu103.pdf"  # Correct path
    text = extract_text_from_pdf(pdf_path)
    print(text[:500])  # Print the first 500 characters of the text
