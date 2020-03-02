
## Convolutional Neural Network

* From Andrew Ng's Deep Learning Specialization class, he discribe the architecture of LeNet-5, and the Hyperparameters.
* In the work, for hands-on experiment, do LeNet-5 on MNIST dataset.

### Digit recognition

This is a digit based dataset for machine learning-based digit recognition.

### CNN dominance

Every task in the field of image recognition is dominated by convolutional neural networks (CNNs)


### Initialization

* Learn about the MNIST dataset (60,000 training example and 10,000 testing examples)
* The original pixel is 20 x 20, then use the pad the white space to 28 x 28 pixel, then finally each picture has 784 pixels.
* Initialize the model with input and output size

1. The input is 784 pixels greyscale size and normalized floating point value
2. The label for an image is a one-hot tensor with 10 classes from 0 ~ 9

`input_dim = 28`, `output_size = 10`


### Reshaping

* In order to use the data with the convolutional neural network, we need to get it into NHWC format.

    - Number of image data sample --> batch size
    - Height of each image
    - Width of each image
    - Channels per image

* Reshape the data, the new shape must be able to contain all the elements from the input tensor.
```
with tf.Session() as sess:
    input_arr = sess.run(inputs)
    reshaped_arr = sess.run(
        tf.reshape(inputs, [-1, 2, 2, 1])
    )
    
```

### Convolution

* We use filters to transform inputs and extract features that allow our model to recognize certain images, the purpose of convolution layers is to extract imporrtant hidden features.
* The filter's weights are `trainable variables`. we can train our neural network to produce filters that are able to extract the most useful hidden features

* Convolution represents how we apply our filter weights to the input data --> element-wise product and apply trainable bias term

### Max Pooling

* Learn about max pooling and its purpose in CNNs
    - Using pooling to further `reduce the size` of the data in `height` and `width` dimensions, and reduce computation cost and `train faster`.
    - `Prevents overfiting`, by extracting only the most salient features and ingoring potential distortions
    
* Three types of pooling: max-pooling, min-pooling, average pooling.
    
    
### Padding

* Increase the ability to learning picture edge information

### Dropout

* Co-adapation refers to when multiple neurons in a layer extract the same, or very similar, hidden features from the input data.
    - waste of computation because of the redundant neurons
    - overfitting if the duplicate extracted features are specific to only the training set

* Dropout is a technics that can reduce overfitting in large neural networks

    - When a fully-connected layer has a large number of neurons, **co-adaptation** is more like to occur.
    - It is a waste of computation
    - It adds more significance to those features for our model, this leads to overfitting

* Definition: `randomly` shut down some fraction (dropout rate) of a layer's neurons to be zero.

    - Hyperparameter = dropout rate
    - the remaining neurons have their values multiplied by 1 / (1-dropout_rate)

### Logits

* We can use `get_logits` , which obtains logits from `dropout`


## Tensorflow version LeNet-5

```
batch_size = 16
# make the batch size
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
        reshaped_inputs = tf.reshape(inputs, [-1, self.input_dim, self.input_dim, 1])
        # batch size is unspecified, then we use -1
        # the first layer has 32 filter
        conv1 = tf.layers.conv2d(reshaped_inputs, 
                                filters=32,
                                kernel_size=[5,5],
                                padding='same',
                                activation=tf.nn.relu,
                                name='conv1')
        
        pool1 = tf.layers.max_pooling2d(
            conv1,
            pool_size=[2,2],
            strides=2,
            name='pool1'
            )
        
        # The second convolution layers has 64 filters
        conv2 = tf.layers.conv2d(
            pool1,
            filters=64,
            kernel_size=[5,5],
            padding='same',
            activation=tf.nn.relu,
            name='conv2')
        
        # max pooling 2
        pool2 = tf.layers.max_pooling2d(
            conv2,
            pool_size=[2,2],
            strides=2,
            name='pool2')
        
        # flatten the layer
        hwc = pool2.shape.as_list()[1:]
        flattened_size = hwc[0] * hwc[1] * hwc[2]
        pool2_flat = tf.reshape(pool2, [-1, flattened_size])
        dense = tf.layer.dense(pool2_flat, 1024, activation=tf.nn.relu, name='dense')
        dropout= tf.layers.dropout(
            dense,
            rate=0.4,
            training=is_training)
        logits = tf.layers.dense(dropout,
            self.output_size,
            name='logits')
        
        return logits

def run_model_setup(self, inputs, labels, is_training):
    logits = self.model_layers(inputs, is_training)
    
    self.probs = tf.nn.softmax(logits, name='probs')
    self.predictions = tf.argmax(
        self.probs, axis=-1, name='predictions')
    class_labels = tf.argmax(labels, axis=-1)
    
    is_correct = tf.equal(
        self.predictions, class_labels)
    
    is_correct_float = tf.cast(
        is_correct,
        tf.float32)
    
    # comput ratio of correct to incorrect predictions
    self.accuracy = tf.reduce_mean(
        is_correct_float)
    
    if self.is_training:
        labels_float = tf.cast(
            labels, tf.float32)
        
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits, 
            labels=labels_float,
            logits=logits
        self.loss = tf.reduce_mean(
            cross_entropy)
        
        adam = tf.train.AdamOptimizer()
        self.train_op = adam.minimize(
            self.loss, global_step=self.global_step)
        

```

## PyTorch Version LeNet-5

* life is short, please use pytorch

```



```