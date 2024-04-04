from fuzzywuzzy import fuzz

class Eval:
    def __init__(self, k):
        self.k = k
    def recall_k(self, test_labels, ret_context):
        ctr = 0
        correct, incorrect = [], []
        for i in range(len(ret_context)):
            done = False
            if isinstance(test_labels[i], float):
                # handle case for when answer is not present in the pdf
                continue
            for j in range(min(self.k,len(ret_context))):
                if fuzz.partial_ratio(test_labels[i], ret_context[i][j])>=90 and len(ret_context[i][j])>=len(test_labels[i])*0.95:
                    # print ("test_labels:", test_labels[i], "\n", "ret_context:", ret_context[i][j])
                    ctr += 1
                    done = True
                    break
                    
            if done == False:
                incorrect.append({test_labels[i]:ret_context[i]})

            else:
                correct.append({test_labels[i]:ret_context[i]})

        return ctr/len(ret_context), incorrect, correct