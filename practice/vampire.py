print("Hey, what's your name?")
name = input()
print("How old are you?")
age = int(input())
if age < 90:
    print("* sigh * " + str(name) + ", I thought you were a vampire for a second there! Thank god!")
elif age > 90:
    print(str(name) + ", you really shouldn't make it so obvious!")
    print("Do you like sunlight? Yes or no?")
    sunlight = input()
    if sunlight == "yes":
        print("You are not a vampire!")
    elif sunlight == "no":
        print("Okay, you are definitely a vampire dude!")
    else:
        print("That's not what I asked for. Nevermind!")
else:
    print("nevermind")
