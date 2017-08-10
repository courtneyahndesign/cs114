print("Hey, what's your name?")
name = input()
print("How old are you?")
age = int(input())
if age < 90:
    print("* sigh * " + str(name) + ", I thought you were a vampire for a second there! Thank god!")
elif age > 90:
    print( str(name) + ", you really shouldn't make it so obvious! It's okay, vampires are welcome here!")
else:
    print("nevermind")
