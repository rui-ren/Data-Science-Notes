
## ResNet

### Deep learning obstacles

* deep models tend to have numerous weight parameters, they take a long time to train

* deep models extract more hidden features than shallow models, they have higher risk of overfitting the training data

-- This two issues can be dealt with relatively seamlessly. Using modern day `GPU` and distributed training (training a model in parallel across multiple processing units) to train faster.

-- overfitting can be reduce by `max pooling`, `dropout`, and `global average pooling`.

### Degradation

* The problem of degradation however, caused the model to have lower accuracy in both training and testing.

### ResNet

* The ResNet model architecture was developed specially to solve the degradation problem, using a residual learning block to counteract degradation.

### ImageNet

* This dataset contains 1.4 million images, with 1.2 M in the training set, 50,000 in the validation set, and the remaining 150,000 in the test set.

* The images are distributed across 1,000 categories.

* ImageNet images have varying heights and widths


### Initialization

* Learn about the ResNet model structure

* Understand the difference between channels-first and channels-last


### Filter and strides

* The first filters starts off at 64, the stride in the first layer might be different
* The remaining filters use 128 filters, the stride is 1


### padding

```
pad_total = kernel_size



```

### Pre-activation

* `covariate shift` occurs when the input data's `distribtion` changes and the model cannot handle the change properly.

    - training a set of only iamges of brown dogs, but test the model on image of yellow dogs. 


* `internal covariate shift` is essentially just a covariate shift that happens between layers of a model since the input of one layer is the output of the previous layer. The weights of a model are constantly being updated, each layer's output distribution will constantly change. However, in models with many layers these incremental changes will eventually add up, and lead to internal covariate shift at deeper layers.

    - Solution to internal covariate shift is `batch normalization`.
    
    - Batch normalization has two trainable variables, $\gamma$ and $\beta$, $BN(X) = \gamma * X + \beta$
    
    - During evaluation, we use the average mean and variance for each batch normalization layer rather than the input data's mean and variance.
    
    
* Pre-activation

when we use batch normalization, we apply it right before an activation function, e.g. ReLU. Normally, the activation function in CNNs comes after each convolution layer -> `Post-activation`

`ResNet Version 1`: Convolution layers -> batch normalization -> ReLU activation.


`ResNet Version 2`: batch normalization -> ReLU activation -> Convolution layers


### Shortcut

* Mapping function: Each ResNet building block takes in an input $\ x$, and produces some output $\ H(x)$, where $\ H$ represents mapping function.

* Identity mapping: just means the `output` for a layer is the `same` as the `input`.

* Residual learning: $ F_B(x) = \ H_B(x) - \ x $, we add a $\ x$ to the block's output. This is referred to as a `shortcut connection`. $\ F_B (X)$ is sknown as `residual learning`.

* Projection shortcut: is the result of applying a convolution layer, with $\ 1x1$ kernels, to the preactivation input data. This convolution layer ensures that the **shortcut** has the same dimensions as the block's output, by using the same stride size and number of filters.

### ResNet Block

* Learning the identity: it is easier to learn the `zero mapping` than the `identity mapping`, just need the weight to be zero. 

* Improving performance: adding many layers to a model and still avoid degradation, by having the additional layers represent identity mappings, and residual learning `increase` model performance when adding many layers.

### Bottlenect

* `ResNet Block` is the main building block for models with fewer than 50 layers, use 3 convolution layers rather than 2.

* `Bottlenect block` : the third convolution layer of a bottleneck block uses four times as many filters as a regular ResNet block.

* 


### Full Model Architecture

* Regularization: Batch normalization has the effect of regularization, thus did not use `dropout` in the model for the calculation
* 