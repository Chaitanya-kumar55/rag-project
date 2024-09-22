from pdf_extractor import extract_text_from_pdf
from text_chunker import chunk_text
from embedding_creator import create_embeddings
from faiss_retriever import create_faiss_index, retrieve_chunks
from text_generator import generate_response

def main(pdf_path, query):
    # Step 1: Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Chunk the text into manageable chunks
    text_chunks = chunk_text(text)
    
    # Step 3: Create embeddings for the text chunks
    embeddings = create_embeddings(text_chunks)
    
    # Step 4: Create a FAISS index for efficient search
    index = create_faiss_index(embeddings)
    
    # Step 5: Retrieve the most relevant chunks based on the query
    retrieved_chunks = retrieve_chunks(query, index, text_chunks)
    
    # Step 6: Generate a response based on the retrieved chunks
    answer = generate_response(retrieved_chunks)
    
    print(f"Query: {query}")
    print(f"Generated Answer: {answer}")

if __name__ == "__main__":
    pdf_path = "your_pdf_file.pdf"  # Path to the PDF file
    query = "What is the main conclusion of the document?"  # Your query
    main(pdf_path, query)
