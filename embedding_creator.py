from sentence_transformers import SentenceTransformer

def create_embeddings(text_chunks):
    """
    Create embeddings for the given text chunks using Sentence-BERT.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Pre-trained model
    embeddings = model.encode(text_chunks, convert_to_tensor=True)
    return embeddings.cpu().detach().numpy()  # Convert to numpy for FAISS

if __name__ == "__main__":
    # Test the function
    sample_chunks = ["This is the first chunk.", "This is the second chunk."]
    embeddings = create_embeddings(sample_chunks)
    print(embeddings)
