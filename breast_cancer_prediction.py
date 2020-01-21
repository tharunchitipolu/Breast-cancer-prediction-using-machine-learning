# -*- coding: utf-8 -*-
"""breast cancer prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z8Ju_hnTAWPbpEW4i1gbWBSlVCXDRztS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('dataset.csv')

df.shape

df.isna().sum()

df = df.dropna(axis=1)

df.shape

df['diagnosis'].value_counts()

df.dtypes

from sklearn.preprocessing import LabelEncoder
labelencoder_Y= LabelEncoder()
df.iloc[:,1]= labelencoder_Y.fit_transform(df.iloc[:,1].values)

df.head(6)

X = df.iloc[:,2:31].values
Y = df.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.75,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Using Support Vector Machine Algorithm
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, Y_train)

Y_predict = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
ac = accuracy_score(Y_test, Y_predict, normalize = True)