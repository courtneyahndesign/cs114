print("How many gallons would you like to convert to liters?")
gallons = input()
liters = int(gallons) * 3.78541
print(str(gallons) + " gallons is " + str(liters) + " liters")

print("How many liters would you like to convert to gallons?")
liters = input()
gallons = int(liters) / 3.78541
print(str(liters) + " liters is " + str(gallons) + " gallons")
