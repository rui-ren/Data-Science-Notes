
## Natural Language Processing

Natural Language Processing (NLP) encompassees any task related to machines learning with natural language, human spoken or written language, related to using machines to process and understand human text/speech.

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
    - Use `NLTK` package to do tokenization.
    - Use `Keras` 
    - Use `Re` regulex to do tokenization
    - `sklearn.preprocessing.text.tokenzier`

```
import tensorflow as tf
tokenizer = tf.keras.preprocessing.text.Tokenizer()
text_corpus = ['bob ate apples, and pears', 'fred ate apples!']
# initialize the object with a text corpus
tokenizer.fit_on_texts(text_corpus)
# convert pieces of text into sequences of tokens
new_texts = ['bob ate pears', 'fred ate pears']
print(tokenizer.texts_to_sequences(new_texts))
# print the word index in the token
print(tokenizer.word_index)
```
    - `Tokenizer` will filter out any punctuation and white space

### Tokenizer parameters

```
import tensorflow as tf
tokenizer = tf.keras.preprocessing.text.Tokenizer(
    oov_token="OOV")
    # parameter num_words can specify the maximum number of vocabulary words to use
    # oov_token can give us the special vocabulary token
text_corpus = ['bob ate apples, and pears', 'fred ate apples!']
# generate the text corpus
tokenizer.fit_on_texts(text_corpus)
print(tokenizer.texts_to_sequences(['bob ate bacon']))
print(tokenizer.word_index)
# {'OOV': 1, 'ate': 2, 'apples': 3, 'bob': 4, 'and': 5, 'pears': 6, 'fred': 7}
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

* An **embedding vector** is a `higher-dimensional vector` representation of a vocabulary word, it can give us a sense of distance and capture relationship between words.
* The basis of embedding vectors comes from the concept of a **target-context** and its **context-target**.


### Skip-gram
* The skip-gram model uses `target-context` training pairs, each pair has a target word as the first element and a context word as the second element, creating a training pair for each context word, it requires much `less` actual data than the CBOW model, it can represent words or phrases better than the CBOW model.


### CBOW -> the Continuous-Bag-of-Words
* `context-target` training pairs, each pair will have all the context words as the first element and the target word as the second element, this is faster to train, for common words, CBOW model can present more accurate embedding for more common words, the context element for the CBOW model contains multiple words, we use the average context embedding vector when training our embedding model.

### Comparison between Skip-gram vs. CBOW
- Skip-gram model creates a training pair for each context word, it requre much less actual data than CBOW model
- CBOW model is faster to train
- Skip-gram model is creating multiple instances of training pairs for each target word, it can represent rarer words or phrases better than CBOW model.
- CBOW model can provide more accurate embeddings for more common words

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

* Sampled softmax: the classes we use to calculate the softmax include the actual context vocabulary word as well as a randomly chosen set of words from entire vocabulary to act as the false labels.
    - sampled softmax loss give good approximation when training
    - when evaluating or dev set, it is best to use full softmax cross entropy loss

* NCE loss: convert the multiclass classification problem into a **binary** classification problem.


### Cosine Similarity

* Vector comparision: the standard way for comparing vector similarity is through `cosine similarity`, actually it is the multiplication of two normalization of vectors, its value is between [-1, 1]

* Correlation: cosine similarity measures the `correlation` between two vectors.


### K-Nearest Neighbors

* Find the top correlated vector


## LSTM for NLP

The main idea of machine learning is in `NLP` is to train a model to understand a text corpus well enought so that it can automatically perform tasks such as `text classification` or `text generation`. 

A language model can tell us the likelihood of each word in a given sentence or text passage based on the words that came before it. We can determine how likely a sentence or text passage is by aggregating its individual word probabilities.

- Text classification: email spam
- Text generation: a language model completes a sentence by generating text based on the incomplete input sentence

### Word probabilities

The purpose of a language model is to assign probabilities to words in sequences of text.


## RNN / LSTM

* Understand the differences between `feed-forward` and `recurrent neural networks`.

* Learn about the long short-term memory(LSTM) cell

    - `MLP` is a type of `feed-forward neural network`: each of its layers is a fixed size, and each layer's output is feed into the next layer as input, good for fixed size input data.
    
    - `recurrent neural networks`: designed to work with sequential data of varying lengths, the main component of a recurrent neural network (RNN) is its `cell`.
    
    - `rolled RNN diagram` consists of a single cell and 3 types of connections, the input, output and recurrent.
    
    - Transition of time step are the connections, `state` gives the cell at the current time step information about the cell inputs and outputs from previous time steps, it is incredibly useful for capturing dependencies in the text that make it easier to calculate probalilities and predictions.

### LSTM

* Specially, it is difficult for RNNs to handle `long-term` dependencies. The solution is to use LSTM. `LSTM` cell is specifically designed to keep track of all the useful dependencies in text sequence.

* Inside of a default RNN cell consists of two fully-connected layers. The first layer has `tanh` activation, and it is used to compute the cell's state at a particular time step, based on the previous state and the time step's input. The second fully-connected layer is unactivated, and it's used to compute the cell's output at the time step. The number of hidden units in the cell as the number of hidden units in the fully-connected layers.

* `LSTM` cell adds a few additional layers to the default RNN cell. These additional layers as `gates`, since they help regulate the information that is added or removed from the cell state. These additional gates gives `LSTM` cells the boost needed to handle long-term dependencies.

* Dropout: the purpose of dropout in the context of RNNs is to regularize the `RNN` during training. 

    - In feed-forward neural network, dropout refers to randomly `dropping` or `zeroing-out` certain hidden neurons during training. The **fraction** of neurons that are randomly dropped out is referred to as the `dropout rate`.
    
    - In recurrent neural networks, we apply dropout to the input and/or output of each cell unit. When dropout is applied to a cell's input/output at a particular time step, the cell's connection at that time step is zero'd out. So whatever, the previous input/output value was, it would be set to 0 due to the dropout. `tf.nn.rnn_cell.DropoutWrapper`, and two parameters `input_keep_prob` and `output_keep_prob`, usually,a good tune point is setting parameter as 0.5.
    

### Multiple layers

* Stacking layers : adding cell layers the model to pick up on more complex features from the input sequence and therefore improve performance when trained on a large enough dataset.

* Add more layers can improve performance on larger datasets but also run the risk of overfitting the data.

### LSTM output

* `tf.nn.dynamic_rnn` is the way for us to create and run an RNN. This function takes two required arguments, the first is the cell object that is used to create the RNN. The second is the `batch of input sequences`, which are usually first converted to word embedding sequences.

* `sequence_length` argument, the function can skip unnecessary computation ofr the padded parts of each sequence, which can greatly reduce training time.


### Calculate loss

* covert LSTM models's outputs into logits
* Use a padding mask to calculate the overall loss

* Logits & Loss: regular softmax cross entropy loss, and fully-connected layer to convert model outputs into logits for each of the possible classes.

* Padding mask: we want to exclude the loss calculated for the padded time steps, since those values are meaningless. Therefore, we use a `padding mask` to zeor-out the loss at padded time steps.

### Predictions

* Calculating probabilities: Converting the RNN's output into logits, we apply the softmax function to the final dimension of the logits.

* word predictions: similar to regular multiclass predictions with an MLP, we calculate the RNNs word predictions by taking the highest probability word at each time step.


### Tensor indexing

* Extract the word predictions for the final time step of each sequence.



    
    
    
    
    
    




