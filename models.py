import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import csv
import pickle

df = pd.read_csv("./Advertising.csv")

X = df.drop(columns = "Sales")
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

filename = "model"
pickle.dump(model, open(filename,'wb'))
