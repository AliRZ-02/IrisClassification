# -----------------------------------------------------------------------
# Ali Raza Zaidi
# December 22 2020
# IrisClassification Project
# -----------------------------------------------------------------------

# Imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import joblib

flower_data = pd.read_csv('../Data/iris-data.csv')

# Input Data
input = flower_data.drop(columns="Class")

# Output Data
output = flower_data["Class"]

# Data Splitting
input_train, input_test, output_train, output_test = train_test_split(input,output,test_size=0.1)

# Training
flower_model = DecisionTreeClassifier()
flower_model.fit(input_train,output_train)

# Testing
predictions = flower_model.predict(input_test)
accuracy = accuracy_score(output_test, predictions)

# Exporting
joblib.dump(flower_model, '../Models/flower-model.joblib')
joblib_model = joblib.load('../Models/flower-model.joblib')

# Tree
tree.export_graphviz(joblib_model,out_file='../Models/flower-model.dot',
                     feature_names=['Sepal-Length','Sepal-Width','Petal-Length', 'Petal-Width'],
                     class_names=sorted(output.unique()),label='all',rounded=True,
                     filled=True)
