from nltk.corpus import wordnet

syn = wordnet.synsets('Computer')
# print(syn)
# print(syn[1].definition())

# synonyms = []
# for s in syn:
#     for lemma in s.lemmas():
#         synonyms.append(lemma.name())

# print(synonyms)

antonyms = []
for s in wordnet.synsets('small'):
    for lemma in s.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
print(antonyms)