
## Introduction 

* Seq2Seq models are used for tasks that involve reading in sequence of text and generating an output text sequence based on the input.

* Application: **Diaglog systems** (chatbots), **text summarization**, and **machine translation** are all seq2seq applications.

* `encoder-decoder` which is specifically designed for seq2seq application.

First, an input sequence is fed to the encoder. The output from the last layer of the encoder becomes the input for the first layer of the decoder. 

The decoder transforms that input back into a text sequence.

### Training data

* Learn about the data used to train a seq2seq model, the training pairs that contain an **input sequence** and an **output sequence**.

* Process input and output sequences into training data

* During training, we perform two task:
    - Input task: extract useful information from the sequence
    - Output task: calculate word **probabilities** at each output time step, using information from the **input sequence** and **previous words** in the output sequence.
    

* Process the output sequence into two separate sequences: the ground truth sequence and the final token sequence.

    - The `ground truth sequence` for a seq2seq model is equivalent to the input sequence for a language model. 
    - `Final token sequence` for a seq2seq model is equivalent to the output sequence when training a language model
    
* SOS and EOS tokens
    - start-of-sequence (SOS)
    - end-of-sequence (EOS)
    - the new vocabulary as the `extended vocabulary`


### Final States

* Learn about the final states for an LSTM and BiLSTM

    - The encoder: is responsible for extracting useful information from the input sequence, for NLP application, the encoder is normally an LSTM or BiLSTM.
    - `LSTM final state`: 
    - `Multi-layer final states`: contains a tuple containing the final state for each layer

* BiLSTM final state

    - The final state of a `BiLSTM` consists of the final state for the forward LSTM and the final state for the backward LSTM.

### Combined state

* Combine the final state for each LSTM and BiLSTM

### Encoder-Decoder

* Model architecture: the encoder portion of the encoder-decoder model in this section is a `BiLSTM`. 

* The decoder portion is just a regular forward LSTM, with the same number of LSTM layers as the encoder.

* What makes an encoder-decoder model so powerful is that the decoder uses the final state of the encoder as its initial state, this gives the decoder access to the information that the encoder extract from the input sequence, which is crucial for good sequence to sequence modeling.



### Attention

* Learn about attention and understand why it is useful. Attention makes use of trainable weights to calculate a context vector, like a mini neural network, input: `decoder's current state` and `encoder outputs`, and use its `trainable weights` to produce a context vector.

* Attention mechanisms: `BahdanauAttention` is additive method and `LuongAttention` is multiplicative method.

    - The difference between the two mechanisms is how they combine the `encoder outputs` and `current time step hidden state` when computing the `context vector`.
    
    - 
    ```
    luong = tf.contrib.seq2seq.LuongAttention(
        num_units,
        combined_enc_outputs,
        memory_sequence_length=input_seq_lens
    )
    ```
    
    ```
    import tensorflow as tf
    dec_cell = tf.nn.rnn_cell.LSTMCell(8)
    dec_cell = tf.contrib.seq2seq.AttentionWrapper(
        dec_cell, # add attention to the decoder cell
        luong,
        attention_layer_size=8
    )
    
    ```
    
### Calculating Loss

* Calculate the training loss based on the model's `logits` and `final token sequences`. using a sparse softmax cross entropy loss based on the logits and final token sequences, and then zero-out the time steps that correspond to padding.

* Final token sequence: 

* Sequence mask: 


### Inference Decoding

* Learn how to perform decoding for inference
* Learn about variable scopes for declaring and retieving variables

* Decoding without ground truth: the input for the decoder at each time is just the decoder's output token from the previous time step.

* `GreedyEmbeddingHelper` is the most commonly used inference helper object. 

* `Greedy decoding` 

### Model Improvement

* Good encoder-decoder model tend to have a large number of weight parameters, since they consist of large `LSTM/BiLSTM` layers. It will take a long time to train `encoder-decoder` model to convergence.

    - Solution: use large batch size during the initial stages of training. 
    - Then reduce the batch size once the model begins to show considerable improvement in reducing the loss function.
    - Solution: start off with a larger learning rate, then gradually decrease the learning rate as the model trains.
    

* Domain-specific strategies: Tweaks the model
    - text summarization: truncate the input text to a maximum length
    - text summarization: set a maximum decoding length when creating summaries.
    - dialog systems: prune out profanity and other words 
    
In all, it is important to understand the seq2seq task's domain prior to building an encoder-decoder model for the task.

    

