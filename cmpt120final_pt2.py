# CMPT FINAL PROJECT PT.2
# Amanda Ngo
# Apr. 10, 2021
# Use a set of data and break it into two lists
# to predict and visualize the data

from sklearn.linear_model import LinearRegression
import turtle

# Create a function which creates a bar when given a height and name
def drawBar(value, percentage):
  # Move the turtle down to write the percentage of the bar
  roma.right(90)
  roma.penup()
  roma.forward(20)
  roma.write(percentage)
  roma.forward(-20)
  roma.pendown()
  roma.left(180)
  roma.fillcolor("lavender")
  roma.begin_fill()
  roma.forward(value)
  # Move the turtle above the bar to print the value
  roma.penup()
  roma.forward(20)
  roma.pendown()
  roma.color("black")
  roma.write(value)
  roma.penup()
  roma.forward(-20)
  roma.pendown()
  roma.fillcolor("lavender")
  roma.right(90)
  roma.forward(60)
  roma.right(90)
  roma.forward(value)
  roma.right(90)
  roma.forward(60)
  roma.right(180)
  # Move forward so that the bars will be placed 10 pixels apart
  roma.forward(70)
  roma.end_fill()
  roma.color("black")

# Open the file and process the data
file = open("SeoulBikeData.csv", encoding="utf8")
readline = file.readline()

# Split the data into an output list and input list
output_list = []
input_list = []
for line in file:
  data = line.strip().split(",")
  output_list.append(float(data[1]))
  gather_list = []
  for i in data[2:10]:
    value = float(i)
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
              "40% - 50%":0,"50% - 60%":0,"60% - 70%":0,
              "70% - 80%":0,"80% - 90%":0,"90% - 100%":0}

# Use a for loop to calculate percentage error and add to dictionary
for i in range(len(outcome)):
  if test_output[i] == 0:
    pass
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

# Create a turtle
roma = turtle.Turtle()
wn = turtle.Screen()

# Set settings for turtle
roma.speed(0)
roma.pensize(3)
roma.penup()
roma.goto(-275,-75)
roma.pendown()

# Draw the bar graph
for i in error_data:
    drawBar(error_data[i],i)
