import nltk
import matplotlib.pyplot as plt
# nltk.download('all')

text = "Someone has told you that words in English can be separated by simply splitting on whitespace. How many times would that heuristic fail for the following text?"

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
tokenized_word = word_tokenize(text)

# print('word_tokenize: ', word_tokenize(text))
# print('sent_tokenize: ', sent_tokenize(text))
# print('FreqDist: ', FreqDist(tokenized_word))

fd = FreqDist(tokenized_word)
print(fd.most_common(3))

fd.plot(30, cumulative=False)
plt.show()