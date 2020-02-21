
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



* 