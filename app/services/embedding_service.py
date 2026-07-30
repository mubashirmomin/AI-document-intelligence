from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def create_embeddings(text_chunks):

    embeddings = embedding_model.encode(
        text_chunks,
        convert_to_numpy=True,
    )

    return embeddings