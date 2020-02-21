## Text classification

* Use **bidirectional** LSTM for text classification. The bidirectional LSTM can be use to separated into positive and negative reviews, `Sentiment Analysis`, `spam filtering` and `automatically flagging inappropriate or harmful social media posts`.


### Sentiment analysis

* An even simpler classification would be to separate the reviews into tow categories: positive and negative.

* The training pairs contains input data and labels.


### Bidirectional LSTM

* It is beneficial to look at the sequence in both the forwards and backwards directions, looking into the past the future to understanding of the text sequence.

* In tensorflow, we can create and run a BiLSTM using `tf.nn.bidirectional_dynamic_rnn`


### Loss

* The loss function is sigmoid, because the intention is to output lable `0` or label `1`. 

### Classification

* change to probability

### Improving the model

* An easy way to imporve the model would be use more LSTM layers or hidden LSTM units.






