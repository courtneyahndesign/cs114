#Save your solution as practice/wall-painting.py. All our friends are re-painting one wall of their rooms. They want us to figure out how much it's going to cost. Assume one gallon of paint covers 400 square feet. Ask the user for: Width of the wall, Height of the wall. How much a gallon of paint costsFigure out then print how much it will cost to paint the wall with one coat.

print("Are you trying to find out how much it will cost to paint your wall? If so, what is the width of the wall in ft?")
width = input()
print("What is the length of the wall in ft?")
length = input()
print("What is the price for gallon?")
price_per_gallon = input()
area = float(width) * float(length)
gallons_used = float(area) / float(400)
total_price = float(gallons_used) * float(price_per_gallon)
print("It will cost $" + str(total_price) + " to paint your wall.")
