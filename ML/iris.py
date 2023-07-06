from sklearn.datasets import load_iris
import pandas as pd
import mglearn
import numpy as np

iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

iris_dataframe=pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)

X_new = np.array([[4.3,2.9,0.7,0.2]])
prediction = model.predict(X_new)
print(prediction)
print(iris_dataset['target_names'][prediction])

y_p = model.predict(X_test)
print(y_p)
print(f"{np.mean(y_p == y_test):.2f}")
print(f"{model.score(X_test, y_test):.2f}")