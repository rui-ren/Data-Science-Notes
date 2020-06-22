from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
import graphviz
import os
from sklearn.model_selection import cross_val_score

os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'


X = [[0, 0], [1, 1,]]
Y = [0, 1]
clf = DecisionTreeClassifier()
clf = clf.fit(X, Y)
tree.plot_tree(clf)
plt.show()

clf.predict([[2., 2.]])
# the classifier for the array
print(repr(clf.predict([[2., 2.]])))
# the probability for each array
print(repr(clf.predict_proba([[2., 2.]])))
clf.predict_proba([[2., 2.]])


######################################################### Multi-Variate classifier ###########################

X, y = load_iris(return_X_y = True)
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

tree.plot_tree(clf)
plt.show()
