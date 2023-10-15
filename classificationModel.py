import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv('heart.csv')


X = dataset.iloc[:, : - 1]
y = dataset.iloc[:, -1]

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = GaussianNB()
model.fit(X, y)

data = {
   "model" : model,
   "scaler": scaler,
   }

with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)