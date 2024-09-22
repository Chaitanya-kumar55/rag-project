from transformers import pipeline

def generate_response(retrieved_chunks):
    """
    Generate a response based on the retrieved text chunks using a summarization model.
    """
    generator = pipeline('summarization', model='facebook/bart-large-cnn')
    context = " ".join(retrieved_chunks)  # Combine the retrieved chunks into context
    response = generator(context, max_length=150)
    return response[0]['summary_text']

if __name__ == "__main__":
    # Test the function
    sample_chunks = ["This is the first chunk.", "This is the second chunk."]
    answer = generate_response(sample_chunks)
    print(answer)
