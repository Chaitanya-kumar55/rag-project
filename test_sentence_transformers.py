from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define some sentences
sentences = ['This is an example sentence', 'Each sentence is converted']

# Compute embeddings
embeddings = model.encode(sentences)

print(embeddings)
