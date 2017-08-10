#utilize the random function to print the user's name a random # of times with a layer of complexity

print("What's your name?")
name = input()
import random
for i in range(1):
    amount = (random.randint(1, 10))
eggs = 0
while eggs < int(amount):
    print(name)
    eggs = eggs + 1
