

#Some supermarkets have automatic change dispensers. Let's write code that figures out how to divvy up an amount of change into the fewest quarters, dimes, nickels, and pennies.Ask for the amount of change to dispense in cents. Assume that the amount input will be less than 100 cents. Calculate the number of quarters necessary first. Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins. This is easiest done by updating a running total of number of cents left to be put into coins. Also remember that the // operator divides and removes any remainder.

print("Don't know what coins to give back to your customer? Please enter the amount of change in cents...")
initialamount = input()
quarters = int(initialamount) // 25
dimes = (int(initialamount) - (int(quarters)) * 25) // 10
nickels = (int(initialamount) - (int(quarters) * 25) - (int(dimes) * 10)) // 5
pennies = (int(initialamount) - (int(quarters) * 25) - (int(dimes) * 10) - (int(nickels) * 5)) // 1
print("You should give them " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickels) + " nickels, and " + str(pennies) + " pennies." )
