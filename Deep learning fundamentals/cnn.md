
## Convolutional Neural Network

* From Andrew Ng's Deep Learning Specialization class, he discribe the architecture of LeNet-5, and the Hyperparameters.
* In the work, for hands-on experiment, do LeNet-5 on MNIST dataset.

### Digit recognition

This is a digit based dataset for machine learning-based digit recognition.

### CNN dominance

Every task in the field of image recognition is dominated by convolutional neural networks (CNNs)


### Initialization

* Learn about the MNIST dataset (60,000 training example and 10,000 testing examples)
* Initialize the model with input and output size

1. The input is 784 pixels greyscale size and normalized floating point value
2. The label for an image is a one-hot tensor with 10 classes

`input_dim = 28`, `output_size = 10`

```
batch_size = 16
dataset = dataset.batch(batch_size)
it = dataset.make_one_hot_iterator()
inputs, labels = it.get_next()
with tf.Session() as sess:
    # Batch of data size 16
    input_arr, label_arr = sess.run(
        (inputs, labels))

import tensorflow as tf

class MNISTModel(object):
    def __init__(self, input_dim, out_size):
        # Constructor
        self.input_dim = input_dim
        self.output_size = output_size
    
    def model_layers(self, inputs, is_training):
        reshaped_input = tf.reshape(inputs, [-1, self.input_dim, self.input_dim, 1])
        conv1 = tf.layers.conv2d(reshaped_inputs, 
                                filters=32,
                                kernel_size=[5,5],
                                padding='same',
                                activation=tf.nn.relu,
                                name='conv1')
        

```

### Reshaping

* In order to use the data with our convolutional neural network, we need to get it into NHWC format.

    - Number of image data sample --> batch size
    - Height of each image
    - Width of each image
    - Channels per image

* Reshape the data
```
with tf.Session() as sess:
    input_arr = sess.run(inputs)
    reshaped_arr = sess.run(
        tf.reshape(inputs, [-1, 2, 2, 1])
    )
    
```

### Convolution

* We use filters to transform inputs and extract features that allow our model to recognize certain images
* The filter's weights are trainable variables. we can train our neural network to produce filters that are able to extract the most useful hidden features

* Convolution represents how we apply our filter weights to the input data --> element-wise product and apply trainable bias term

### Max Pooling

* Learn about max pooling and its purpose in CNNs
    - Using pooling to further reduce the size of the data in height and width dimensions, and reduce computation cost and train faster.
    - Prevents overfiting, by extracting only the most salient features and ingoring potential distortions
    
    
### Padding
* Increase the ability to learning picture edge information

### Dropout

* Dropout is a technics that can reduce overfitting in large neural networks

    - When a fully-connected layer has a large number of neurons, **co-adaptation** is more like to occur.
    - It is a waste of computation
    - It adds more significance to those features for our model, this leads to overfitting

* Definition: randomly shut down some fraction of a layer's neurons to be zero.

    - Hyperparameter = dropout rate
    - the remaining neurons have their values multiplied by 1 / (1-dropout_rate)

### Logits

* We can use `get_logits` , which obtains logits from `dropout`

