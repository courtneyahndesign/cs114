print("Hey, what's your name?")
name = input()
print("How old are you?")
age = input()
newage = int(age) + 1
message = name + ", guess what? You're going to be a whopping " + str(newage) + " years old in a year!"
print(message)
