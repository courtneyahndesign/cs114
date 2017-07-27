

#Some supermarkets have automatic change dispensers. Let's write code that figures out how to divvy up an amount of change into the fewest quarters, dimes, nickels, and pennies.Ask for the amount of change to dispense in cents. Assume that the amount input will be less than 100 cents. Calculate the number of quarters necessary first. Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins. This is easiest done by updating a running total of number of cents left to be put into coins. Also remember that the // operator divides and removes any remainder.

print("Enter amount of change in cents")
initialamount = input()
quarters = int(initialamount) // 25
print("You will have " + str(quarters) + " quarters" )
dimes = (int(initialamount) - (int(quarters)) * 25) // 10
print("You will have " + str(dimes) + " dimes" )
nickels = (int(initialamount) - (int(quarters) * 25) - (int(dimes) * 10)) // 5
print("You will have " + str(nickels) + " nickels" )
pennies = (int(initialamount) - (int(quarters) * 25) - (int(dimes) * 10) - (int(nickels) * 5)) // 1
print("You will have " + str(pennies) + " pennies" )
