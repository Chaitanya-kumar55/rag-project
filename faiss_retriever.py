import faiss
from sentence_transformers import SentenceTransformer

def create_faiss_index(embeddings):
    """
    Create a FAISS index from the given embeddings.
    """
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)  # L2 distance metric
    index.add(embeddings)  # Add embeddings to index
    return index

def retrieve_chunks(query, index, text_chunks, model_name='sentence-transformers/all-MiniLM-L6-v2', top_k=5):
    """
    Retrieve the most relevant chunks for the given query.
    """
    model = SentenceTransformer(model_name)
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().detach().numpy()
    D, I = index.search(query_embedding, top_k)  # Top-k relevant chunks
    return [text_chunks[i] for i in I[0]]

if __name__ == "__main__":
    # Test the function
    sample_chunks = ["This is the first chunk.", "This is the second chunk."]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sample_chunks, convert_to_tensor=True).cpu().detach().numpy()
    index = create_faiss_index(embeddings)
    query = "first chunk"
    retrieved_chunks = retrieve_chunks(query, index, sample_chunks)
    print(retrieved_chunks)
