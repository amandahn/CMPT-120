# CMPT FINAL PROJECT PT.1
# Amanda Ngo
# Apr. 1, 2021
# Use a random set of data to train and predict a function

import random
from sklearn.linear_model import LinearRegression

# Create a program that creates list of randomized lists
train_input= []
for i in range(100):
  randlist = [random.randint(0,1000) for i in range(3)]
  train_input.append(randlist)

# Using the randomized lists, combine and create an output
train_output = []
for i in train_input:
  outputvalue = [i[0] + 2*(i[1]) + 3*(i[2])]
  train_output += outputvalue

# Train to predict the coefficients
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)

# Test the prediction
X_test = [[10,20,30]]
outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_
print("Prediction: " + str(outcome))
print("Coefficients: " + str(coefficients))
