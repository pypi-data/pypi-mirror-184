import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('6.csv')
print("The first 5 Values of data is :\n", data.head())
X = data.iloc[:, :-1]
print("\nThe First 5 values of the train attributes is\n", X.head())

Y = data.iloc[:, -1]
print("\nThe First 5 values of target values is\n", Y.head())

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.20)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)
pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score,recall_score,precision_score,confusion_matrix
print("Accuracy is:", accuracy_score(Y_test,pred)*100)
print('Recall: ', recall_score(Y_test, pred))
print('Precision: ', precision_score(Y_test, pred))
print('Confusion Matrix: \n', confusion_matrix(Y_test, pred))

