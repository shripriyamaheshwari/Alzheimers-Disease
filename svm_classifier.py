import sklearn
import scipy.io as sio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC # "Support Vector Classifier"
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.metrics import classification_report

dataset = pd.read_csv('svm.csv')


dataset.head()

print(dataset.head())

data = dataset.drop('Group', axis=1)
data = data.drop('Gene Name', axis=1)
data = data.replace(np.NaN, 0)
X = data[2:]
print(dataset.head())
datay = dataset['Group']
y = datay[2:]

train, test, train_labels, test_labels = train_test_split(X,y,test_size=0.33,random_state=2)
#print(type(train_labels))
#print(test_labels)
# Initialize our classifier
# Create Decision Tree classifer object

clf =SVC(kernel='rbf', C=2)
#clf = SVC(kernel = 'linear')
#clf = SVC(kernel = 'poly')
#clf = SVC(kernel = 'sigmoid')
#clf = DecisionTreeClassifier()
# Train Decision Tree Classifer
clf = clf.fit(train,train_labels)

#Predict the response for test dataset
y_pred = clf.predict(test)



#print(len(y),sum(y==1))
print(len(test_labels),sum(test_labels==1))
print(len(y_pred),sum(y_pred==1))
#print(y_pred)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",accuracy_score(test_labels, y_pred))
print(classification_report(test_labels, y_pred))
