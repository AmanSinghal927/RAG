import faiss
import torch

class FlatIdx:
    def __init__(self, d):
        self.d = d
        self.index = faiss.IndexFlatL2(d)
    
    def add_idx(self, sentence_embeddings):
        self.index.add(sentence_embeddings)
    
    def faiss_st_inference(self, model, indexed_data, query_data, k=4):
        if isinstance(query_data, list):
            ret_context = []
            for query in query_data:
                xq = model.encode([query])
                if isinstance(xq, torch.Tensor):
                    xq = xq.detach().numpy()
                D, I = self.index.search(xq, k)
                retrieved_items = [indexed_data[i] for i in list(I[0])]
                ret_context.append(retrieved_items)
            return ret_context  
        
    def faiss_tfidf_inference(self, vectorizer, indexed_data, query_data, k=4):
        if isinstance(query_data, list):
            ret_context = []
            for query in query_data:
                xq = vectorizer.transform([query])
                xq = xq.toarray().astype('float32')
                D, I = self.index.search(xq, k)
                retrieved_items = [indexed_data[i] for i in list(I[0])]
                ret_context.append(retrieved_items)
            return ret_context   

    def faiss_dragon_inference(self, model, tokenizer, indexed_data, query_data, k=4):
        if isinstance(query_data, list):
            ret_context = []
            for query in query_data:
                query_input = tokenizer(query, return_tensors='pt')
                xq = model(**query_input).last_hidden_state[:, 0, :]
                if isinstance(xq, torch.Tensor):
                    xq = xq.detach().numpy()
                D, I = self.index.search(xq, k)
                retrieved_items = [indexed_data[i] for i in list(I[0])]
                ret_context.append(retrieved_items)
            return ret_context  

