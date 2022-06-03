# CMPT FINAL PROJECT PT.3
# Amanda Ngo
# Apr. 11, 2021
# Build another model which predicts and visualizes data
# using a different dataset

from sklearn.linear_model import LinearRegression
import turtle

# Create a function which creates a bar when
# given a height, name, and colour
def drawBar(height, value, percentage, fillcolor):
  # Move down to write which percentage is being shown
  # then move back to the original position
  roma.right(90)
  roma.penup()
  roma.forward(20)
  roma.write(percentage)
  roma.forward(-20)
  roma.pendown()
  # Draw one side of the bar
  roma.left(90)
  roma.fillcolor(fillcolor)
  roma.begin_fill()
  roma.left(90)
  roma.forward(height)
  # Move downwards and display the amount of error
  roma.penup()
  roma.forward(-15)
  roma.right(90)
  roma.forward(5)
  roma.pendown()
  roma.color("black")
  roma.write(value)
  roma.fillcolor(fillcolor)
  roma.penup()
  # Move back to the previous position and finish drawing the bar
  roma.forward(-5)
  roma.left(90)
  roma.forward(15)
  roma.pendown()
  roma.right(90)
  roma.forward(60)
  roma.right(90)
  roma.forward(height)
  roma.right(90)
  roma.forward(60)
  roma.right(180)
  # Move forward so that the bars will be placed 10 pixels apart
  roma.forward(70)
  roma.end_fill()
  roma.color("black")

# Open the file
file = open("dataset_Facebook.csv")
readline = file.readline()

# Sort the data from the file into two lists
output_list = []
input_list = []
for line in file:
  data = line.strip("").split(";")
  output_list.append(int(data[0]))
  gather_list = []
  for i in data[2:]:
    # Replace blank spaces with zero
    if i == '':
      gather_list.append(0)
    else:
      value = int(i)
      gather_list.append(value)
  input_list.append(gather_list)

# Split the output list and input list into training and test lists
list_split = round(len(input_list)*0.8)
train_input = input_list[0:list_split]
train_output = output_list[0:list_split]
test_input = input_list[list_split:]
test_output = output_list[list_split:]

# Use the scikit learn module to predict the output values
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)

outcome = predictor.predict(X=test_input)
coefficients = predictor.coef_

# Print the predictions and coefficients
print("Prediction: " + str(outcome))
print("Coefficients: " + str(coefficients))

# Create an empty dictionary for percentage error
error_data = {"0% - 10%":0,"10% - 20%":0,"20% - 30%":0,"30% - 40%":0,
"40% - 50%":0,"50% - 60%":0,"60% - 70%":0,"70% - 80%":0,
"80% - 90%":0,"90% - 100%":0}

# Use a for loop to calculate percentage error and add to dictionary
passed = 0
for i in range(len(outcome)):
  if test_output[i] == 0:
    passed += 1
  else:
    error = (abs(test_output[i] - outcome[i])/test_output[i])*100
    if 0 <= error <= 10:
      error_data["0% - 10%"] += 1
    elif 10 < error <= 20:
      error_data["10% - 20%"] += 1
    elif 20 < error <= 30:
      error_data["20% - 30%"] += 1
    elif 30 < error <= 40:
      error_data["30% - 40%"] += 1
    elif 40 < error <= 50:
      error_data["40% - 50%"] += 1
    elif 50 < error <= 60:
      error_data["50% - 60%"] += 1
    elif 60 < error <= 70:
      error_data["60% - 70%"] += 1
    elif 70 < error <= 80:
      error_data["70% - 80%"] += 1
    elif 80 < error <= 90:
      error_data["80% - 90%"] += 1
    elif 90 < error <= 100:
      error_data["90% - 100%"] += 1

# Use a for loop to find the highest value key in dictionary
max_value = 0
for i in error_data:
  if error_data[i] > max_value:
    max_value = error_data[i]

# Divide the max value into seven parts
threshold = round(max_value/7)

# Create a turtle
roma = turtle.Turtle()
wn = turtle.Screen()

# Set settings for turtle
turtle.bgcolor("azure")
roma.speed(0)
roma.pensize(3)
roma.penup()
roma.goto(-275,-75)
roma.pendown()

# Draw a X axis
roma.left(180)
roma.forward(15)
roma.write("0")
roma.forward(-15)
roma.right(90)
height = threshold*10
# For every threshold increment, write the value
for i in range(1,8):
  roma.forward(height)
  roma.left(90)
  roma.forward(15)
  roma.write(threshold*i)
  roma.forward(-15)
  roma.right(90)
  # Write the values removed due to /0 error
  if i == 3:
    roma.left(90)
    roma.penup()
    roma.forward(165)
    roma.write("Outputs not included: "+str(passed))
    roma.forward(-165)
    roma.right(90)
    roma.pendown()
  # Title of axis
  if i == 4:
    roma.left(90)
    roma.penup()
    roma.forward(155)
    roma.write("Error value",font=("Arial", 12, "bold"))
    roma.forward(-155)
    roma.right(90)
    roma.pendown()
roma.forward(30)
roma.stamp()
roma.right(180)
roma.forward((height*7)+ 30)
roma.left(90)
roma.forward(10)

# Draw a y axis and title
roma.forward(320)
roma.right(90)
roma.penup()
roma.forward(40)
# Title of axis
roma.write("Percentage of error",font=("Arial", 12, "bold"))
roma.forward(-40)
roma.left(180)
roma.forward((height*7)+ 30)
# Title of graph
roma.write("dataset_Facebook.csv",font=("Arial", 15, "bold"))
roma.forward(-((height*7)+30))
roma.pendown()
roma.right(90)
roma.forward(390)
roma.forward(-700)

# Draw the bar graph with changing colors
# depending on the # of errors in the percentage group
for i in error_data:
  bar_height = error_data[i]*10
  if error_data[i] == 0:
    roma.right(90)
    roma.penup()
    roma.forward(20)
    roma.write(i)
    roma.left(180)
    roma.forward(30)
    roma.write(error_data[i])
    roma.forward(-10)
    roma.right(90)
    roma.pendown()
    roma.forward(70)
  elif 0 < error_data[i] <= threshold:
    drawBar(bar_height,error_data[i],i,"thistle")
  elif threshold < error_data[i] <= threshold*2:
    drawBar(bar_height,error_data[i],i,"light sky blue")
  elif threshold*2 < error_data[i] <= threshold*3:
    drawBar(bar_height,error_data[i],i,"aquamarine")
  elif threshold*3 < error_data[i] <= threshold*4:
    drawBar(bar_height,error_data[i],i,"lemon chiffon")
  elif threshold*4 < error_data[i] <= threshold*5:
    drawBar(bar_height,error_data[i],i,"peach puff")
  elif threshold*5 < error_data[i] <= threshold*6:
    drawBar(bar_height,error_data[i],i,"light coral")
  elif threshold*6 < error_data[i] <= max_value:
    drawBar(bar_height,error_data[i],i,"pink")
