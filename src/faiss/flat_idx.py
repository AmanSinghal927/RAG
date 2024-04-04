import faiss

class FlatIdx:
    def __init__(self, d):
        self.d = d
        self.index = faiss.IndexFlatL2(d)
    
    def add_idx(self, sentence_embeddings):
        self.index.add(sentence_embeddings)
    
    def faiss_inference(self, model, indexed_data, query_data, k=4):
        if isinstance(query_data, list):
            ret_context = []
            for query in query_data:
                xq = model.encode([query])
                D, I = self.index.search(xq, k)
                retrieved_items = [indexed_data[i] for i in list(I[0])]
                ret_context.append(retrieved_items)
            return ret_context    

