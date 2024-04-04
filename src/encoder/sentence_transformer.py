from sentence_transformers import SentenceTransformer

class Encoder:
    def __init__(self, data):
        self.data = data
        self.embedding = None
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    def get_embeddings(self):
        self.embedding = self.model.encode(self.data)
        