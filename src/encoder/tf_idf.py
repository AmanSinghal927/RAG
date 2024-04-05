from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text_no_punctuation = text.translate(translator)
    tokens = nltk.word_tokenize(text_no_punctuation)
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word not in stop_words]
    return ' '.join(tokens)

class Encoder:
    def __init__(self, data):
        self.data = data
        self.embedding = None
        self.model = TfidfVectorizer()

    def get_embeddings(self, clean = False):
        if clean:
            self.data = [preprocess_text(x) for x in self.data]
        tfidf_vectors = self.model.fit_transform(self.data)
        self.embedding = tfidf_vectors.toarray()
        