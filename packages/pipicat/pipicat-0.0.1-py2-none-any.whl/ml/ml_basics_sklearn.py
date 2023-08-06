# This is a show case for using methods from sklearn for classification
# Yi Ding

# Load data and import library
from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
boston = load_boston()
digits = load_digits()
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from my_cross_val import my_cross_val
import matplotlib.pyplot as plt

# Machine Learning Type
CLASSIFICATION = 0
REGRESSION = 1


# Create array to Create Boston50 and Boston75
r = np.array(boston.target)

# Find 50th and 75th percentile
tau50 = np.median(r)
tau75 = np.percentile(r, 75)

# Construct Boston50 and Boston75
y50 = np.empty([r.size, 1])
y75 = np.empty([r.size, 1])
for i in range(0, r.size):
    if r[i] < tau50:
        y50[i] = 0
    else:
        y50[i] = 1
for i in range(0, r.size):
    if r[i] < tau75:
        y75[i] = 0
    else:
        y75[i] = 1          

k = 10


# Cross-validation
lr = LinearRegression()
y = boston.target
y_pred = cross_val_predict(lr, boston.data, y, cv=10)
# Draw figure
fig, ax = plt.subplots()
ax.scatter(y, y_pred, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

# Classification
# Test models with each data set
X = [boston.data,boston.data,digits.data]
y = [y50,y75,digits.target]
method = [LinearSVC,SVC,LogisticRegression]
methodStr = ["LinearSVC","SVC","LogisticRegression"]
datasetStr = ["Boston50","Boston75","Digits"]
for i in range(0,3):
    for j in range(0,3):
        errRat = my_cross_val(method[i],X[j],y[j],k,CLASSIFICATION)
        print(str(i*3+j+1)+". "+methodStr[i]+" with "+datasetStr[j])
        print("Test set error rate:")
        print(errRat)
        print("Mean error rate over " +str(k)+" folds")
        print(np.mean(errRat));
        print("Std of the error rate over "+str(k)+" folds")
        print(np.std(errRat));
        print(" ")
        
# Regression
method = LinearRegression
X = boston.data
y = r
k = 2
err_rat = my_cross_val(method,X,y,k,REGRESSION)
print("Test set error rate:", err_rat)