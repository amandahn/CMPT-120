# Vaccination Analysis (Pt. 2)
# Amanda Ngo
# Feb. 18, 2021
# Write a program that outputs:
# - the vaccination percentage of a chosen country
# - worldwide vaccination average
# - country with lowest vaccinated population
# - country with highest vaccinated population

# Open file and process header
file = open("vaccinations.csv")
readline = file.readline().strip().split(",")
country_data = {}

# STEP 1: Show the vaccination percentage of a chosen country

for line in file:
 data = line.split(",")
 country = data[0].upper()
 vaccinations = data[8]

 # Make it so that values of zero or empty values are not accepted
 # but hundreth decimals are processed and added
 if vaccinations == '' or vaccinations == "0":
   pass
 else:
  country_data[country] = int(float(vaccinations)*100)/100

# Ask the user for the data they want
country_wanted = input("Which country would you like data for? ").upper().strip()

# Create conditional statements based on if the country data is available
# and print statements accordingly
if country_wanted in country_data:
  print(country_wanted, "has vaccinated {:.1f}% of their population." 
  .format(country_data[country_wanted]))
else:
  print("There is no data for the country", country_wanted)

# STEP 2: Calculate the worldwide average 

# Intialize worldwide average variable
total_vaccinated = 0

# Create a for loop which adds together all avaible data
# and divides by amount of countries
for country in country_data:
  total_vaccinated += country_data[country]
total_vaccinated = total_vaccinated/len(country_data)

# Print the total
print("The worldwide vaccination average is {:.1f}%.".format(total_vaccinated))

# STEP 3: Find the country with the lowest percentage

# Initialize lowest percentage variable
lowest_percentage = 100

# Create a for loop which replaces the lowest percentage variable
# with any value that is smaller
for country in country_data:
  if country_data[country] < lowest_percentage:
    lowest_percentage = country_data[country]
    lowest_percentage_country = country
  else:
    pass
# Print the country with the lowest percentage
print("The country with the lowest vaccination percentage is", 
lowest_percentage_country, "with {:.1f}%".format(lowest_percentage))

# STEP 4: Find the country with the highest vaccination percentage

# Initialize highest percentage variable
highest_percentage = 0

# Create a for loop which replaces the highest percentage variable
# with any value that is larger
for country in country_data:
  if country_data[country] > highest_percentage:
    highest_percentage = country_data[country]
    highest_percentage_country = country
  else:
    pass

# Print the country with the highest percentage
print("The country with the highest vaccination percentage is", 
highest_percentage_country, "with {:.1f}%".format(highest_percentage))
