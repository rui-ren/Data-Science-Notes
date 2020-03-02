
## Feature Importance
* Understand how to measure each dataset feature's importance in making model predictions

* Use the matplotlib pyplot API to save a feature importance plot to a file

### Determine importance features

For analyzing the importance of features, after training XGBoost model, we can view the relative importance of each dataset feature using `feature_importances_` property of the model.

```
model = xgb.XGBClassifier()
# predefine data and labels
model.fit(data, labels)

# array of feature importances
print(model.feature_importances_)

# predefined data and labels (for regression)
model = xgb.XGBRegressor()
model.fit(data, labels)
xgb.plot_importance(model)
plt.show()

```

* Notice `importance_type` to change the metric: 
1. The `F-score` is a standardized measurement of a feature's importance, based on the specified importance metric

2. `Information gain`


### Hyperparameter Tuning

* Apply grid search cross-validation to `XGBoost` model

```
model = xgb.XGBClassifier()
params = {
    'max_depth': range(2, 5)
}

from sklearn.model_selection import GridSearchCV
cv_model = GridSearchCV(model, params, cv=4, iid=False)
## be aware that the default k-fold for cross-validation is 4


# predefined data and labels
cv_model.fit(data, labels)

# cross validation model 
cv_model.best_params_['max_depth']

# new_data contains 2 new data observations
# cv_model.predict(new_data)
```

