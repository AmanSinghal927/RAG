# DONE
1. Added basic implementation.ipynb - Recall@4 with sentence transformer and IndexFlatL2 is 28.57% | considering partial fuzzy match only if retrieved context is longer 0.95 times ground truth
2. Added Chunking - Recall@4 with sentence transformer and IndexFlatL2 is 42.85% | considering partial fuzzy match only if retrieved context is longer 0.95 times ground truth
3. Chunking + Dragon - 7%, direct dense retrieval may not be the answer
4. Chunking + TF-IDF - vocab size is 4.5K - 64.28%; Insight: Dense retrievers are not good at exact word matches
  - Tried variations with k=15 and cleaning (lowercase, no stopwords, stemming lemmatization); also varaince threshold -> what works is (lowercase, no stopwords)
  - error analysis: 3 no answers, 1 segmentation error, 1 multiple answers
5. Chunking + TF-IDF + Thresholding for no-answer 78.57% @ k=15
  - threshold for no answer: [1.5917805, 1.6717079, 1.2556686] median value in tf-idf 1.5917805
6. Including table queries and data from raw_text - 73.9% recall@10
- MRR is 0.46 (MRR criteria, partial fuzzy matches allowed only when len(pred)>=0.95*len(ground_truth)

7. 2-stage system with reranking based on dragon, MRR is 0.65, 73.9% recall@10
   
9. Along with PDF with no labels, MRR is 0.5, 70.0% recall@10

# TODO

2. Try other Indexes to check latency when done with everything else 

3. Use DR--185549702_INTRO as val
   
~~5. Better chunking for paras with words like following/below in the last sentence~~
   
~~7. Tabular format -> One table and its header is one chunk? Or should be do this row-wise?~~
   
~~9. OOP code organization~~
    
11. Documentation

12. Try other embedders like splade ~~& dragon~~

~~13. No match threshold~~
    
~~15. Multi-answer query evaluation: Maybe MRR would take care of this as well~~

# Improvements
- Logical table storing e.g. table_name.col_name.row_name = cell_value
- Discuss Lettau’s framework using various mathematical formulae and What legislative suggestions pertaining to workplace sexual harassment does the firm provide in its submission?; require multiple contexts while the system works for 2, for 1 we need better parsing results, especially current model like llm_sherpa give a lot of weightage to spatial features like centering and mis-classify paras as headers


    
