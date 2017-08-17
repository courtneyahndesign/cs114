#Make a program that asks a user their name and returns a randomly chosen "fortune" response from the "magic 8 ball". Make 9 different possible "fortunes".
#Save your program as 'magic8ball.py'

print("What's your name?")
name = input()

print( str(name) +", I am your magic 8 ball! Give me a question and I will tell you the truth!")
answer = input()

import random
for i in range(1):
    amount = (random.randint(1, 9))

if amount == 1:
    print("Of course!")
elif amount == 2:
    print("Nope, definitely not")
elif amount == 3:
    print("Busy...try again later!")
elif amount == 4:
    print("Never!")
elif amount == 5:
    print("Duh, yes!")
elif amount == 6:
    print("That's a stupid one. Try again.")
elif amount == 7:
    print("Yep bro!")
elif amount == 8:
    print("Not today dude!")
elif amount == 9:
    print("Hahaha, you wish!")
