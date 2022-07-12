# Vaccination Analysis (Pt. 1)
# Amanda Ngo
# Feb. 16, 2021
# Write a program that outputs the vaccination percentage
# of the world

# Open file and process header
file = open("vaccinations.csv")
readline = file.readline().strip().split(",")
country_info = {}

for line in file:
 data = line.split(",")
 country = data[0]
 vaccinations = data[8]
 if vaccinations == '' or vaccinations == "0":
   pass
 else:
  country_info[country] = int(float(vaccinations)*100)/100
for country in country_info:
  print(country+": {:.1f}".format(country_info[country]))
