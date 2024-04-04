import pandas as pd
from src.rechunker import Rechunker
from src.encoder.sentence_transformer import Encoder
from src.faiss.flat_idx import FlatIdx
from utils.utils import flatten_list, logger
from src.eval import Eval
import os
import json



if __name__=="__main__":
    ground_truth_path = r"C:\Users\J C SINGLA\Downloads\External - take_home_challenge_(withJSONs)\take_home_challenge_(withJSONs)\document_questions.xlsx"
    
    chunker = Rechunker("/Users")
    all_data_sherpa, filenames_sherpa = chunker.get_paras()
    all_data_sherpa = flatten_list(all_data_sherpa)
    embeddings = Encoder(all_data_sherpa)
    embeddings.get_embeddings()
    index = FlatIdx(embeddings.embedding.shape[1])
    index.add_idx(embeddings.embedding)
    # print ("index.is_trained ", index.index.is_trained, "\n")
    print ("index.ntotal ", index.index.ntotal, "\n")
    ground_truth = pd.read_excel(ground_truth_path)
    ground_truth_text = ground_truth[ground_truth["complexity"]=="text"].copy()
    test_data = list(ground_truth_text["relevant questions"])
    test_labels = list(ground_truth_text["answer"])
    retrieved_items = index.faiss_inference(embeddings.model, all_data_sherpa, test_data)
    print ("len(retrieved_items)", len(retrieved_items))
    metric = Eval(k=4)
    recall, incorrect, correct = metric.recall_k(test_labels, retrieved_items)
    print (recall)
    logger(correct, incorrect)


