#utilize the random function to print the user's name a random # of times with a layer of complexity

print("What's your name?")
name = input()
length = len(name)

import random
for i in range(1):
    amount = (random.randint(1, 10))

newamount = int(amount) + int(length)

eggs = 0
while eggs < int(newamount):
    print(name)
    eggs = eggs + 1
