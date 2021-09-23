#Programmers: Peter and Victoria
#Course: CS151, Dr.Rajeev
#Date: 9/23/21
#Lab Number: 2
#Program Inputs: Number of births, deaths, and migrations per second, the current population, and the desired number of years in the future.
#Program Outputs: The population after specified years.

#The program asks for number of births, deaths, and migrations per second, the current population, and the desired number of years in the future, and converts them to floats.

print("Specify number of births, deaths, and migrations per second, the current population, and the desired number of years in the future.")
currentpop = float(input("Input current population: "))
births = float(input("Input births per second: "))
deaths = float(input("Input deaths per second: "))
migrations = float(input("input migrations per second: "))
years = float(input("Input desired number of years into the future: "))

#The program estimates the population

population = currentpop + ((births + migrations - deaths) * 31536000 * years)

#The program outputs the estimated population

print("The estimated population after " + str(years) + " years is " + str(population) + ("."))