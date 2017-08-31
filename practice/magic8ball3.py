

print("What's your name?")
name = input()

print( str(name) +", I am your magic 8 ball! Give me a question and I will tell you the truth!")
answer = input()

messages = ["Of course!",
    "Nope, definitely not",
    "Busy...try again later!",
    "Never!",
    "Duh, yes!",
    "That's a stupid one. Try again.",
    "Yep bro!",
    "Not today dude!",
    "Hahaha, you wish!"]

import random
for i in range(1):
    amount = (random.randint(1, 9))

def choosemessage(messages):
    if amount == 1:
        randommessage = messages[0]
    elif amount == 2:
        randommessage = messages[1]
    elif amount == 3:
        randommessage = messages[2]
    elif amount == 4:
        randommessage = messages[3]
    elif amount == 5:
        randommessage = messages[4]
    elif amount == 6:
        randommessage = messages[5]
    elif amount == 7:
        randommessage = messages[6]
    elif amount == 8:
        randommessage = messages[7]
    elif amount == 9:
        randommessage = messages[8]
    return randommessage

def main():
    finalmessage = choosemessage(messages)
    return print(finalmessage)

main()
