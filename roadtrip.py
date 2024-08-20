"""
Python for everyone 1: week 2 - variables
Alena Hemminger
Goal: compute and compare mileage and fuel use across small and large cars
"""

print("Road trip efficiency compariasons:")
#__dunder__ this is a dunder (built in) variable
#assigning a string literal on the right to the variable on the left
small_vehicle = "2021 Volkswagen Jetta"
large_vehicle = "2014 Chevy Captiva"
small_vehicle_mpg = 34
large_vehicle_mpg = 26.0

small_vehicle_url = "https://www.caranddriver.com/volkswagen/jetta-2021"
large_vehicle_url = "https://www.kbb.com/chevrolet/captiva-sport/2014/"

print("The", small_vehicle, "can drive", small_vehicle_mpg, "miles per gallon of gasoline")
print("Info can be found at", small_vehicle_url)

print("The", large_vehicle, "can drive", large_vehicle_mpg, "miles per gallon of gasoline")
print("Info can be found at", large_vehicle_url)

#additional logic warnings extension
print(" ")
if small_vehicle_mpg < 20 or large_vehicle_mpg < 20:
  if small_vehicle_mpg < 20:
    print("Warning: The", small_vehicle, "has a mpg of", small_vehicle_mpg, "which is not very fuel efficient!")
  elif large_vehicle_mpg < 20:
    print("Warning: The", large_vehicle, "has a mpg of", large_vehicle_mpg, "which is not very fuel efficient!")
  else:
    print("Warning: Both the", small_vehicle, "and the", large_vehicle, "has a mpg less than 20, which is not very fuel efficient!")
else:
  print("Both the", small_vehicle, "and the", large_vehicle, "have mpg rates higher than 20 which is great!")
  print("On behalf of global climate, thank you for being fuel efficient!")

print(" ")
print("------------MILEAGE--------------")

print("Road trip! How many miles? (decimal places okay)")
#read keyboard input, turn to float, store in trip_miles
trip_miles = float(input())
#gallons computed by dividing trip length by mileage
small_vehicle_gallons = trip_miles / small_vehicle_mpg
large_vehicle_gallons = trip_miles / large_vehicle_mpg

print("The", small_vehicle, "will require", small_vehicle_gallons, "gallons of fuel to travel", trip_miles, "miles")
print("The", large_vehicle, "will require", large_vehicle_gallons, "gallons of fuel to travel", trip_miles, "miles")

print( )
#comparison b/t small and large car gallons needed
diff_gas_use = large_vehicle_gallons - small_vehicle_gallons
print("Comparing the two cars, the", large_vehicle, "will require", diff_gas_use, "more gallons of fuel than the", small_vehicle)

print(" ")
print("------------COSTS--------------")

print("What is the average cost for a gallon of gasoline for this trip?")

ppg = float(input())

total_small_cost = small_vehicle_gallons * ppg
total_large_cost = large_vehicle_gallons * ppg
diff_cost = total_large_cost - total_small_cost

print("In the", small_vehicle, "the trip will cost around", total_small_cost, "dollars.")
print("In the", large_vehicle, "the trip will cost around", total_large_cost, "dollars.")

print(" ")

print("Comparing the two cars, the ", large_vehicle, "will cost", diff_cost, "dollars more than the", small_vehicle)

print(" ")
print("------------TIME--------------")

highway_speed = 70
local_speed = 45

#get speed adjustments
print("Assuming the average highway speed is", highway_speed, "and the average local speed is", local_speed, ",")
print("How many mph do you go over the speed limit on highways?")
highway_speed_adjust = float(input())
print("How many mph do you go over the speed limit on local roads?")
local_speed_adjust = float(input())

adjusted_highway = highway_speed + highway_speed_adjust
adjusted_local = local_speed + local_speed_adjust

#find out amount of time spent on highways
print("What percent of your trip will be on the highway/ interstate?")
highway_percent = float(input())

total_highway_miles = (highway_percent / 100) *trip_miles
total_local_miles = trip_miles-total_highway_miles

total_highway_mins = total_highway_miles * (adjusted_highway/60)

total_local_mins = total_local_miles * (adjusted_local/60)

total_mins = total_highway_mins + total_local_mins
total_hrs = total_mins / 60

print("Both the", small_vehicle, "and the", large_vehicle, "will take", total_mins, "minutes, or", total_hrs, "hours to travel", trip_miles, "miles")