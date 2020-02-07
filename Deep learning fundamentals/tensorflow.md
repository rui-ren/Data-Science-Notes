## Tensorflow

### Model initialization

* Placeholder is a `placeholder` for the input data and labels

1. tf.placeholder takes in a required first argument and two keyword arguments(shape, name)

2. 

```
def init_inputs(input_size):
    inputs = tf.placeholder(
    tf.float32, shape=(None, input_size), name='inputs')
    return inputs
    

```


### Logits

1. Fully-connected layer
2. Weighted connections
3. Logits
4. Regression

```
def model_layers(inputs, output_size):
    logits = tf.layers.dense(inputs, output_size,
                            name='logits')
    return logits
```

### Metrics
`tf.nn.sigmoid`

`tf.reduce_mean`

```
probs = tf.nn.sigmoid(logits)
rounded_probs = tf.round(probs)
predictions = tf.cast(rounded_probs, tf.int32)
is_correct = tf.equal(predictions, labels)
is_correct_float = tf.cast(is_correct, tf.float32)
accuracy = tf.reduce_mean(is_correct_float)

```

### Loss as error `L1` and `L2`
### Cross entropy `log loss`

### Optimization `gradient descent`
`tf.train.GradientDescentOptimizer`
set the learning rate, the better way is use `Adam` optimizer.  `tf.train.AdamOptimizer`


## Evaluation

### Evaluating using accuracy
After training a model, it is a good idea to evaluate its performance. we can split trainig set (80%) validation set(10%) and test set (10%)

```
feed_dict = {
    inputs: test_data,
    labels: test_labels
}

eval_acc = sess.run(accuracy, feed_dict = feed_dict)

```

### Different amount of data


## Linear Limitations

### Linear decision boundary


## Hidden layer

* add a hidden layer to the model's layers
* understand the purpose of non-linear activations
* learn about the ReLU activation function

### Why a single layer is limited
* a single layer logits is directly connected to the input and output using a linear combination. As such, single layer perceptron can model any linear boundary. However, the equation of the circle boundary cannot be modeled.

### Hidden layers
* Single linear combination doesn't work, what can we do? We can add more linear combination, and non-linearities. 

### Non-linearity
* `tanh`,  `ReLU`, `sigmoid`, `leaky-ReLU`, `Softmax`
* The simplicity of ReLU, specifically with respect to its gradient, allows it to avoid the vanishing gradient problem.

```
def model_layers(inputs, output_size):
    logits = tf.layers.dense(inputs, output_size,
                             name= 'logits')
    hidden1 = tf.layers.dense(logits, 5, activation=tf.nn.relu, name='hidden1)
    return hiddden1
```

### Multiclass

* understand the difference between binary and multicalss classification
* One-hot
* adding hidden layers

```
# be aware that the 3 layers might be good to try
def model_layers(inputs, output_size):
    hidden1 = df.layers.dense(inputs, 5,
                            activation=tf.nn.relu,
                            name='hidden1')
    hidden2 = df.layers.dense(hidden2, 5,
                            activation=tf.nn.relu,
                            name='hidden2')
    logits = tf.layers.dense(hidden2, output_size,
                            name='logits')
    return logits
```

### Softmax
* softmax function is used to convert a neural network from binary to multiclasss classification
* model's prediction now becomes the class with the highest probability using `tf.argmax`

```
t = tf.constant([[0.4, -0.8, 1.3],
                 [0.2, -1.2, -0.4]])
softmax_t = tf.nn.softmax(t)
sess = tf.Session()
```

