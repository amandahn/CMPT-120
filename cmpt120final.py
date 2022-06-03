# CMPT FINAL PROJECT 
# Amanda Ngo
# Apr. 13, 2021
# Create a program which takes user input and instructions
# to predict and visualize data

from sklearn.linear_model import LinearRegression
import turtle

# Create a function which creates a bar when
# given a value, name, and colour
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

# Ask the user about data info
input_file = input("What is the name of your file?(Include .csv, file\
 cannot have spaces.) ").strip()
input_split = input("How is your file split?(ie. , or ;) ").strip()
input_prediction = int(input("What is the prediction \
column of your CSV file? ").strip())

# Ask if the prediction data is continuous, and process data accordingly
continuous = input("Are the input columns continous?(Y/N) ").upper().strip()

# If the input is continuous, ask for the two columns
if continuous == "Y":
  indice_1 = int(input("Please input the first indice. ").strip())
  indice_2 = int(input("Please input the last indice. ").strip())

  # Open the file and process the data
  file = open(input_file, encoding = "utf8")
  readline = file.readline()

  # Split the data into an output list and input list
  output_list = []
  input_list = []
  for line in file:
    data = line.strip().split(input_split)
    output_list.append(float(data[input_prediction]))
    gather_list = []
    for i in data[indice_1:indice_2]:
      if i == '':
        gather_list.append(0)
      else:
        value = float(i)
        gather_list.append(value)
    input_list.append(gather_list)

# If the input is not continous, ask the user to input
# the columns, and put it into a list
elif continuous == "N":
  indice_list = []
  indices = input("Please input the columns used,\
 seperated by commas. ").strip()
  indice_list = indices.split(",")

  # Open the file and process the data
  file = open(input_file, encoding = "utf8")
  readline = file.readline()

  # Split the data into an output list and input list
  output_list = []
  input_list = []
  for line in file:
    data = line.strip().split(input_split)
    output_list.append(float(data[input_prediction]))
    gather_list = []
    for i in indice_list:
      indice = int(i)
      if data[indice] == '':
        gather_list.append(0)
      else:
        value = float(data[indice])
        gather_list.append(value)
    input_list.append(gather_list)

# Create training and test lists
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
  # If the test output is 0, ignore and add to passed
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
# In the case that the result number results in a 0 round
if threshold == 0:
  threshold = 1

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
# Scale the height if threshold value is too small
if 5 < threshold <= 10:
  height = threshold*5
elif 1 < threshold <= 5:
  height = threshold*10
elif threshold == 1:
  height = 50
else:
  height = threshold
# For every threshold increment, write the value
for i in range(1,8):
  roma.forward(height)
  roma.left(90)
  roma.forward(20)
  roma.write(threshold*i)
  roma.forward(-20)
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
roma.write(input_file,font=("Arial", 15, "bold"))
roma.forward(-((height*7)+30))
roma.pendown()
roma.right(90)
roma.forward(390)
roma.forward(-700)

# Draw the bar graph with changing colors
# depending on the # of errors in the percentage group
for i in error_data:
  # Scale the height if the max value is low enough
  if 5 < threshold <= 10:
    bar_height = error_data[i]*5
  elif 1 < threshold <= 5:
    bar_height = error_data[i]*10
  elif threshold == 1:
    bar_height = error_data[i]*50
  else:
    bar_height = error_data[i]
  if error_data[i] == 0:
    roma.right(90)
    roma.penup()
    roma.forward(20)
    roma.write(i)
    roma.left(180)
    roma.forward(40)
    roma.write(error_data[i])
    roma.forward(-20)
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
