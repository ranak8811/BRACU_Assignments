import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Someone has told you that words in English can be separated by simply splitting on whitespace. How many times would that heuristic fail for the following text?"

stop_words = set(stopwords.words('english'))
# print(stop_words)

tokenize_words = word_tokenize(text)
tokenize_words_without_stop_words = []

for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)

# print('Tokenizing words without stop words: %s' % tokenize_words_without_stop_words)

print('stop words which got removed: ' , set(tokenize_words) - set(tokenize_words_without_stop_words))

print('tokenize words: ', tokenize_words)
print('tokenize words_without_stop_words: ', tokenize_words_without_stop_words)