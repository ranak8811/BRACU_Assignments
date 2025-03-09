from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = "Someone has told you that words in English can be separated by simply splitting on whitespace. How many times would that heuristic fail for the following text?"
demo_words = ['playing', 'happiness', 'going', 'having', 'doing', 'yes', 'no', 'I', 'had', 'haved', 'codings', 'programming', 'code', 'program', 'went', 'should']

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# for word in demo_words:
#     print(word, stemmer.stem(word), lemmatizer.lemmatize(word, 'v'))

sia = SentimentIntensityAnalyzer()
# print(sia.polarity_scores('Programming is fun'))
# print(sia.polarity_scores('You behaved very bad today'))
print(sia.polarity_scores('This is neigther good nor bad'))