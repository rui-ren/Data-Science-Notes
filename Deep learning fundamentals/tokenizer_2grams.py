
## Tokenizer

# ngrams are one of the ways to maintain context information as data pass through your pipeline

from nltk import ngrams

message = "Thomas Jefferson began building Monticello at the age of 26."
n = 2
# The nltk will return a generator for python, instead of the entire list
# save momery and storage
twograms = ngrams(message.split(), n)

print(list(twograms))

"""
[('Thomas', 'Jefferson'), ('Jefferson', 'began'), ('began', 'building'), ('building', 'Monticello'), ('Monticello', 'at'), ('at', 'the'), ('the', 'age'), ('age', 'of'), ('of', '26.')]

"""

## Join them together
twograms = list(ngrams(message.split(), 2))
two_grams = [" ".join(i) for i in twograms]
print(two_grams)

"""
['Thomas Jefferson', 'Jefferson began', 'began building', 'building Monticello', 'Monticello at', 'at the', 'the age', 'age of', 'of 26.']
"""
import nltk
nltk.download('stopwords')
# get the English corpus -->
stop_words = nltk.corpus.stopwords.words("english")
print(len(stop_words))
print(stop_words[:7])


# Stemming
def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$', word)[0][0].strip('"') for word in phrase.lower().split()])

stem('houses')

# use the nltk package

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
''.join([stemmer.stem(w).strip("") for w in "dish washer's washed dishes".split()])


### TF-IDF

from nltk.tokenize import TreebankWordTokenizer
sentence = """ThE faster Harry got to the store, the faster Harry, the faster, would get home"""

# seems like the prifix tree in the algorithm class
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
print(tokens)

from collections import Counter
bag_of_words = Counter(tokens)
print(bag_of_words)


words = """A kite is a tethered heavier-than-air craft with wing surfaces that react against the air to create lift and drag. A kite consists of wings, tethers and anchors. Kites often have a bridle and tail to guide the face of the kite so the wind can lift it.[2] Some kite designs don’t need a bridle; box kites can have a single attachment point. A kite may have fixed or moving anchors that can balance the kite. One technical definition is that a kite is “a collection of tether-coupled wing sets“.[3] The name derives from its resemblance to a hovering bird.[4]

The lift that sustains the kite in flight is generated when air moves around the kite's surface, producing low pressure above and high pressure below the wings.[5] The interaction with the wind also generates horizontal drag along the direction of the wind. The resultant force vector from the lift and drag force components is opposed by the tension of one or more of the lines or tethers to which the kite is attached.[6] The anchor point of the kite line may be static or moving (e.g., the towing of a kite by a running person, boat, free-falling anchors as in paragliders and fugitive parakites[7][8] or vehicle).[9][10]

The same principles of fluid flow apply in liquids, so kites can be used in underwater currents, but there are no everyday uses as yet.[11][12]

Man-lifting kites were made for reconnaissance, entertainment and during development of the first practical aircraft, the biplane.

Kites have a long and varied history and many different types are flown individually and at festivals worldwide. Kites may be flown for recreation, art or other practical uses. Sport kites can be flown in aerial ballet, sometimes as part of a competition. Power kites are multi-line steerable kites designed to generate large forces which can be used to power activities such as kite surfing, kite landboarding, kite fishing, kite buggying and snow kiting."""

## TF --> term frequency
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
stop_words = nltk.corpus.stopwords.words("english")
tokens = tokenizer.tokenize(words)
tokens = [i for i in tokens if i not in stop_words]
token_counts = Counter(tokens)

## Vectorization
document_vector = []
doc_length = len(tokens)
for key, value in token_counts.most_common():
    document_vector.append(value/doc_length)

document_vector 


###

docs = ["The faster Harry got to the store, the faster and faster Harry would get home."]
docs.append("Harry is hairy and faster than Jill.")
docs.append("Jill is not as hairy as Harry.")

doc_tokens = []
for doc in docs:
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]

# sum them up and return a single list  
all_doc_tokens = sum(doc_tokens, [])
# reduce the order
lexicon = sorted(set(all_doc_tokens))

from collections import OrderedDict
# sorted based on ASC II number
zero_vector = OrderedDict((token, 0) for token in lexicon)

import copy
doc_vectors = []
for doc in docs:
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    doc_vectors.append(vec)

import math
def cosine_sim(vec1, vec2):
    "Let's convert our dictionaries to lists for easier matching"
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
    
    # dot product
    dot_prob = 0
    for i, v in enumerate(vec1):
        dot_prob += v * vec2[i]
    
    # the mode
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    
    return dot_prod / mag_1 / mag_2
    

words_kites = """Kites were invented in Asia, though their exact origin can only be speculated. The oldest depiction of a kite is from a mesolithic period cave painting in Muna island, southeast Sulawesi, Indonesia, which has been dated from 9500–9000 years B.C.[13] It depicts a type of kite called kaghati, which are still used by modern Muna people.[14] The kite is made from kolope (forest tuber) leaf for the mainsail, bamboo skin as the frame, and twisted forest pineapple fiber as rope, though modern kites use string.[15]

In China, the kite has been claimed as the invention of the 5th-century BC Chinese philosophers Mozi (also Mo Di, or Mo Ti) and Lu Ban (also Gongshu Ban, or Kungshu Phan). Materials ideal for kite building were readily available including silk fabric for sail material; fine, high-tensile-strength silk for flying line; and resilient bamboo for a strong, lightweight framework. By 549 AD paper kites were certainly being flown, as it was recorded that in that year a paper kite was used as a message for a rescue mission. Ancient and medieval Chinese sources describe kites being used for measuring distances, testing the wind, lifting men, signaling, and communication for military operations. The earliest known Chinese kites were flat (not bowed) and often rectangular. Later, tailless kites incorporated a stabilizing bowline. Kites were decorated with mythological motifs and legendary figures; some were fitted with strings and whistles to make musical sounds while flying.[16][17][18]"""


words_kites = words_kites.lower()
intro_tokens = tokenizer.tokenize(words_kites)
kite_history = words.lower()

history_tokens = tokenizer.tokenize(kite_history)
intro_total = len(intro_tokens)
history_total = len(history_tokens)

intro_tf = {}
history_tf = {}
intro_counts = Counter(intro_tokens)
history_counts = Counter(history_tokens)
intro_tf['kite'] = intro_counts['kite'] / intro_total
history_tf['kite'] = history_counts['kite'] / history_total

num_docs_containing_and = 0
for doc in [intro_tokens, history_tokens]:
    if 'kite' in doc:
        num_docs_containing_and += 1
        
num_docs = 2
intro_idf = {}
history_idf = {}

intro_idf['kite'] = num_docs / num_docs_containing_and
history_idf['kite'] = num_docs / num_docs_containing_and

intro_tfidf = {}

intro_tfidf['kite'] = intro_tf['kite'] * intro_idf['kite']


################################### Latent Semantic Analysis ##################
import numpy as np

### Weighted tf-idf
topic = {}
tfidf = dict(list(zip('cat dog apple lion NYC love'.split(), np.random.rand(6))))

topic['petness'] = (.3 * tfidf['cat'] + .3 * tfidf['dog'] + 0 * tfidf['apple'] + 0 * tfidf['lion'] + .2 * tfidf['NYC'] + .2 * tfidf['love'])
topic['animalness'] = (.1 * tfidf['cat'] + .1 * tfidf['dog'] + 0.1 * tfidf['apple'] + 0.5 * tfidf['lion'] + .1 * tfidf['NYC'] + .1 * tfidf['love'])
topic['cityness'] = (.0 * tfidf['cat'] + .1 * tfidf['dog'] + 0.2 * tfidf['apple'] + 0.1 * tfidf['lion'] + .5 * tfidf['NYC'] + .1 * tfidf['love'])


word_vector = {}
word_vector['cat'] = .3 * topic['petness'] + .1 * topic['animalness'] + 0 * topic['cityness']
word_vector['dog'] = .3 * topic['petness'] + .1 * topic['animalness'] + 0.1 * topic['cityness']
word_vector['apple'] = .0 * topic['petness'] + .1 * topic['animalness'] + 0.2 * topic['cityness']
word_vector['lion'] = .0 * topic['petness'] + .5 * topic['animalness'] + 0.1 * topic['cityness']
word_vector['NYC'] = -.2 * topic['petness'] + .1 * topic['animalness'] + 0.5 * topic['cityness']
word_vector['love'] = .2 * topic['petness'] + .1 * topic['animalness'] + 0.1 * topic['cityness']


















