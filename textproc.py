from sklearn.datasets import load_files
import re
from nltk.corpus import stopwords
def proccessText(rutaNoticias):
        newsData = load_files(rutaNoticias, encoding='latin-1')
        print(newsData.target_names)
        X, y, filenames, targetNames = newsData.data, newsData.target, newsData.filenames, newsData.target_names
        documents = []
        from nltk.stem import WordNetLemmatizer
        stemmer = WordNetLemmatizer()
        for sen in range(0, len(X)):
            # Remove all the special characters
            document = re.sub(r'\W', ' ', str(X[sen]))
            # remove all single characters
            document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
            # Remove single characters from the start
            document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
            # Substituting multiple spaces with single space
            document = re.sub(r'\s+', ' ', document, flags=re.I)
            # Removing prefixed 'b'
            document = re.sub(r'^b\s+', '', document)
            # Converting to Lowercase
            document = document.lower()
            # Lemmatization
            document = document.split()
            document = [stemmer.lemmatize(word) for word in document]
            document = ' '.join(document)
            documents.append(document)
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(max_features=18, min_df=5, max_df=0.7, stop_words=stopwords.words('spanish'))
        X = vectorizer.fit_transform(documents).toarray()

        from sklearn.feature_extraction.text import TfidfTransformer
        tfidfconverter = TfidfTransformer()
        X = tfidfconverter.fit_transform(X).toarray()
        return X,y, filenames, targetNames