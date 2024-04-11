from sentence_transformers import SentenceTransformer

class Encoder:
    def __init__(self):
        self.embedding = None
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    def get_embeddings(self, data):
        embedding = self.model.encode(data)
        return embedding
        