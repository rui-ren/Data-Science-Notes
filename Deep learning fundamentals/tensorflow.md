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
