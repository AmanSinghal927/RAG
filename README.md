# DONE
1. Added basic implementation.ipynb - Recall@4 with sentence transformer and IndexFlatL2 is 28.57% | considering partial fuzzy match only if retrieved context is longer 0.95 times ground truth
2. Added Chunking - Recall@4 with sentence transformer and IndexFlatL2 is 42.85% | considering partial fuzzy match only if retrieved context is longer 0.95 times ground truth
3. Chunking + Dragon - 7%, direct dense retrieval may not be the answer
4. Chunking + TF-IDF - vocab size is 4.5K - 64.28%

# TODO

2. Try other Indexes to check latency when done with everything else 

3. OCR for DR--185549702_INTRO
   
~~5. Better chunking for paras with words like following/below in the last sentence~~
   
7. Tabular format -> One table and its header is one chunk? Or should be do this row-wise?
   
9. OOP code organization
    
11. Documentation

12. Try other embedders like splade & dragon
