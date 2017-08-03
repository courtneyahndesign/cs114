#Save your solution as practice/madlib.py.
#Make a simple madlib filling program. Use the madlib:
#The NOUN jumped over the ADJ NOUN.
#Prompt the user to input those three placeholder words, save them in variables, interpolate them into the madlib, then print the final madlib.

print("Let's make a mad lib! First, give me a noun!")
noun1 = input()
print("Alright, that's good, how about an adjective?")
adj1 = input()
print("Good one! Let's do a verb!")
verb1 = input()
print("That's lame, but whatever...noun, please?")
noun2 = input()
print("You're getting better at this, but that's not saying much...give me an adjective!")
adj2 = input()
print("Better, but not the best. Go ahead and give me another verb.")
verb2 = input()
print("Alright, are you ready for this?")
response = input()
print(str(response) + "?!! Well, I'm doing it regardless of your response anyways!")
print("The " + str(adj2) + " " + str(noun1) + " can " + str(verb2) + " like no other! On the other hand, the " + str(adj1) + " " + str(noun2) + " can " + str(verb1) + " like everybody else!")
