def chunk_text(text, chunk_size=100):
    """
    Split the extracted text into smaller chunks.
    """
    paragraphs = text.split('\n\n')  # Split by paragraphs
    chunks = [paragraphs[i:i+chunk_size] for i in range(0, len(paragraphs), chunk_size)]
    return [" ".join(chunk) for chunk in chunks]

if __name__ == "__main__":
    # Test the function
    sample_text = "This is a sample text.\n\nThis is another paragraph."  # Example text
    chunks = chunk_text(sample_text)
    print(chunks)
