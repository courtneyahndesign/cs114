#Make a program that asks a user their name and returns a randomly chosen "fortune" response from the "magic 8 ball". Make 9 different possible "fortunes".

#Use functions with a main() function. You can refactor your previous Magic 8 ball program or write a new one from scratch.

print("What's your name?")
name = input()

print( str(name) +", I am your magic 8 ball! Give me a question and I will tell you the truth!")
answer = input()

import random
for i in range(1):
    amount = (random.randint(1, 9))

def messages(amount):
    if amount == 1:
        randomamount = "Of course!"
    elif amount == 2:
        randomamount = "Nope, definitely not"
    elif amount == 3:
        randomamount = "Busy...try again later!"
    elif amount == 4:
        randomamount = "Never!"
    elif amount == 5:
        randomamount = "Duh, yes!"
    elif amount == 6:
        randomamount = "That's a stupid one. Try again."
    elif amount == 7:
        randomamount = "Yep bro!"
    elif amount == 8:
        randomamount = "Not today dude!"
    elif amount == 9:
        randomamount = "Hahaha, you wish!"
    return randomamount

def main():
    finalmessage = messages(amount)
    return print(finalmessage)

main()
