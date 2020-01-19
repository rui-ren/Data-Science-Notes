
## XGBoost 

* XGBoost, a state-of-the-art data science library for performing classification and regression.

* XGBoost performed an extremely efficient version of gradient boosted trees. **faster**

### Gradient boosted trees

1. We could continuously increase the maximum depth of a decision tree to fit larger datasets, but decision trees with many nodes tend to overfit the data.

2. Gradient boosting to combine many decision trees into a single models for classification or regression. Gradient boosting starts off with a single decision tree, then iteratively add more decision trees to the overall model to correct the model's errors on the training dataset
.

### XGBoost basic
The basic data structure for `XGBoost` is `DMatrix`, which represents a data matrix, can be constructed from Numpy arrays.

```
dtrain = xgb.DMatrix(data, label=labels)  

# training parameters
params = {
    'max_depth': 0,
    'objective': 'binary:logistic'
}

print('Start training)
bst = xgb.train(params, dtrain)
print('Finish trainig')

```

### Procedure to setup xgboost

```
# STEP 1: set up DMatrix
import xgboost as xgb
dtrain = xgb.DMatrix(data, label=labels)

# STEP 2: parameters setup
params = {
    'max_depth': 2,
    'objective': 'multi:softmax',
    'num_class': 3
}

# STEP 3: train model
bst = xgb.train(params, dtrain)

# STEP 4: Predict
dpred = xgb.DMatrix(new_data)
predictions = bst.predict(dpred)
```

### Cross-validation

* use `cross-validation` to tune the model

```
dtrain = xgb.DMatrix(data, label=labels)
params = {
    'max_depth': 2,
    'lambda': 1.5,
    'objective': 'binary:logistic'
}

cv_results = xgb.cv(params, dtrain)
# this is the cross-validation method, k-fold default is 3
# there also has num_boost_round specifies the number of boosting iterations
```

### Storing booster
* use `save_model` to save the model's binary data

```
# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
    'max_depth': 3,
    'objective': 'binary:logistic'
}
bst = xgb.train(params, dtrain)

# new data observations
dpred = xgb.DMatrix(new_data)
# save model
bst.save_model('new_model')
# load model --> 
# before loading the model, we need to call the object
new_bst = xgb.Booster()
new_bst = xgb.load_model('new_model')
```

### Create Sklearn like API

* `wrapper` `XGBClassifier`

```
# call the object
model = xgb.XGBClassifier()
# predefined data and labels
model.fit(data, labels)
# new_data predicition
predictions = model.predict(new_data)
```

* `wrapper` `XGBRegressor`
```
model = xgb.XGBRegressor(max_depth=2)
# predefine data and lables
model.fit(data, labels)

# new_data contains 2 new data observations
predictions = model.predict(new_data)

```


