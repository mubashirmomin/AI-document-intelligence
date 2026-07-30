from app.services.embedding_service import create_embeddings


# Sample chunks (similar to what chunking_service will produce)
text_chunks = [
    "Artificial intelligence is a field of computer science.",
    "Machine learning allows computers to learn from data.",
    "The heart pumps blood throughout the human body."
]


# Create embeddings
embeddings = create_embeddings(text_chunks)


# Print results
print("Type of embeddings:", type(embeddings))

print("Shape of embeddings:", embeddings.shape)

print("\nFirst embedding vector:")
print(embeddings[0])