
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
