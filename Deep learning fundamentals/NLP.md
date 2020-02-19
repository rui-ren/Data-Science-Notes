
## Natural Language Processing

Natural Language Processing (NLP) encompassees any task related to machines learning with natural language, human spoken or written language. 

* Topic: **translating** between language, speech, recognition, text analysis, and automatic text generation, in general **spoken** or **written data**.

* Process documents of text into embedding vectors
* Build a variety of different LSTM models for tasks ranging from text classification to text generation and machine translation.

### Word embeddings

* using **word embeddings** to give **numeric vector** representations of words.

### Vocabulary

We can use the **vocabulary** to find **the number of times** each word appears in the corpus, figure out which words are the most common or uncommon, and filter each text document based on the words that appear in it.

* Corpus is a set of **texts** used for the task
* **Word-based** vocabulary is the set of unique words used in the text corpus
* **Character-based** vocabulary is the unique character in the text corpus

### Tokenization

* Tokenization is to represent a piece of text to a vector/list of its vocabulary words

### Tokenizer object
* `TensorFlow` we can convert a text corpus into tokenized sequences using `Tokenizer` object.

```
import tensorflow as tf
tokenizer = tf.keras.preprocessing.text.Tokenizer()
text_corpus = ['bob ate apples, and pears', 'fred ate apples!']
tokenizer.fit_on_texts(text_corpus)
tokenizer.fit_on_texts(text_corpus)
new_texts = ['bob ate pears', 'fred ate pears']
print(tokenizer.texts_to_sequences(new_texts))
print(tokenizer.word_index)
```

### Tokenizer parameters

```
import tensorflow as tf
tokenizer = tf.keras.preprocessing.text.Tokenizer(
    oov_token="OOV")
    # parameter num_words can specify the maximum number of vocabulary words to use
    # oov_token can give us the special vocabulary token
text_corpus = ['bob ate apples, and pears', 'fred ate apples!']
tokenizer.fit_on_texts(text_corpus)
print(tokenizer.texts_to_sequences(['bob ate bacon']))
print(tokenizer.word_index)

```

```
import tensorflow as tf

class EmbeddingModel(object):
    def __init__(self, vocab_size, embedding_dim):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=self.vocab_size)
    def tokenize_text_corpus(self, texts):
        self.tokenizer.fit_on_texts(texts)
        sequence = self.tokenizer.texts_to_sequences(texts)
        return sequence
```

### Embeddings

* An **embedding vector** is a higher-dimensional vector representation of a vocabulary word, it can give us a sense of distance and capture relationship between words.
* The basis of embedding vectors comes from the concept of a **target word** and its **context window**.


### Skip-gram
* The skip-gram model uses target-context training pairs, each pair has a target word as the first element and a context word as the second element, creating a training pair for each context word, it requires much less actual data than the CBOW model, it can represent words or phrases better than the CBOW model



### CBOW -> the Continuous-Bag-of-Words

* context-target training pairs, each pair will have all the context words as the first element and the target word as the second element, this is faster to train, for common words, CBOW model can present more accurate embedding for more common words.


### Embedding Matrix

```
import tensorflow as tf
emb_mat = tf.get_variable('v1', shape=(5,10))
word_ids = tf.constant([0,3])  # create the lookup value
emb_vecs = tf.nn.embedding_lookup(emb_mat, word_ids)

```


### Candidat sampling
* 


### Embedding loss

* Sampled softmax

* NCE loss 





