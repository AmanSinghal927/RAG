from transformers import AutoTokenizer, AutoModel
import torch
tokenizer = AutoTokenizer.from_pretrained('facebook/dragon-plus-query-encoder')
query_encoder = AutoModel.from_pretrained('facebook/dragon-plus-query-encoder')
context_encoder = AutoModel.from_pretrained('facebook/dragon-plus-context-encoder')

class Encoder:
    def __init__(self):
        self.context = None
        self.query = None
        self.q_embedding = None
        self.c_embedding = None
        self.tokenizer = tokenizer
        self.query_encoder = query_encoder
        self.context_encoder = context_encoder

    def concat_embeddings(self, data, sz = (0, 768)):
        ctx_emb = torch.empty(sz)
        for i in range(len(data)):
            ctx_input = tokenizer(data[i:i+1], padding=True, truncation=True, return_tensors='pt', max_length = 512)
            temp_emb = context_encoder(**ctx_input).last_hidden_state[:, 0, :]
            ctx_emb = torch.cat((ctx_emb, temp_emb), dim=0)
        return ctx_emb

    def get_embeddings(self, data, stage = "context"):
        if stage == "context":
            self.context = data
            return self.concat_embeddings(data)

        elif stage == "query":
            self.query = data
            return self.concat_embeddings(data)
