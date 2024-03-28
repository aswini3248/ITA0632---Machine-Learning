import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = pd.read_csv("C:/Users/aswin/Documents/ML/iris.csv")
x = iris.drop("species", axis=1)
y = iris["species"]
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(x_new)
print("Prediction: {}".format(prediction))
