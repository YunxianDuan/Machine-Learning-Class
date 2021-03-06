from sklearn import datasets, metrics
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

Treasury = pd.read_csv("F:/MSFE/machine learning in Fin lab/HW2/Treasury Squeeze test - DS1(1).csv" )
# Create feature and target arrays
X = Treasury.iloc[:, 2:11]
y = Treasury.iloc[:, 11]

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Standardizing the features:
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

k_range = range(1, 26)
scores = []
plt.title('k-NN: Varying Number of Neighbors')
# Create a k-NN classifier with k neighbors: knn
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    # Fit the classifier to the training data
    knn.fit(X_train_std, y_train)
    y_pred = knn.predict(X_test_std)
    scores.append(metrics.accuracy_score(y_test, y_pred))

# Generate plot
plt.plot(k_range, scores, marker='o', label='Testing Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

print("My name is Yunxian Duan")
print("My NetID is: yunxian2")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")
print(k_range[scores.index(max(scores))])
print(max(scores))