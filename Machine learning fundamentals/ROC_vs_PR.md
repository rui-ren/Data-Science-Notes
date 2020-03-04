### ROC vs PR

Reference ![https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/]

* (Receiver of Characteristics) ROC and Precision-Recall Curves provide a diagnostic tool for binary classification models

* ROC AUC and Precision-Recall AUC provide scores that summarize the curves and can be used to compare classifiers.

* ROC curves and ROC AUC can be optimistic on severely imbalanced classification problems with few samples of minority class

#### ROC Curves and ROC AUC

An ROC curve is a plot that summarizes the performance of a binary classification model on the **positive** class.

**ROC Curve**: Plot of `False Rate (x-axis)` vs `True Positive Rate (y-axis)`

The true positive rate is a fraction calculated as the total number of **true positive predictions** divided by the sum of the true positives and the false negatives (e.g. **all examples in the positive class**). The true positive rate is referred to as the sensitivity or the recall.

True_Positive_Rate = True_Positive / (True_Positive / False_Negative)


We can think of the plot as the fraction of correct predictions for the positive class (y-axis) versus the fraction of errors for the negative class (x-axis).


