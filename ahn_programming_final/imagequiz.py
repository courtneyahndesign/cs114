import tkinter as tk

root = tk.Tk()
root.geometry('{}x{}'.format(700, 700))
root.title("Images & Tkinter")

images = ["dog1.gif", "dog2.gif", "dog3.gif", "dog4.gif", "dog5.gif", "dog6.gif", "dog7.gif", "dog8.gif", "dog9.gif", "dog10.gif", "final.gif"]

question = tk.Label(root,text = "What breed is this dog?",font = ("Avenir"))
question.pack()

image = tk.PhotoImage(file= images[0])
label = tk.Label(image=image)
label.pack()

def question2():
    image.configure(file= images[1])
    answer_one.configure(text = "Standard American Eskimo Dog", command = question3)
    answer_two.configure(text = "Alaskan Malamute", command = question3_right)
    answer_three.configure(text = "American Foxhound", command = question3)
    answer_four.configure(text = "American Staffordshire Terrier", command = question3)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question2_right():
    image.configure(file= images[1])
    answer_one.configure(text = "Standard American Eskimo Dog", command = question3)
    answer_two.configure(text = "Alaskan Malamute", command = question3_right)
    answer_three.configure(text = "American Foxhound", command = question3)
    answer_four.configure(text = "American Staffordshire Terrier", command = question3)
    question.configure(text = "Correct! \n What breed is this dog?")

def question3():
    image.configure(file= images[2])
    answer_one.configure(text = "American Water Spaniel", command = question4)
    answer_two.configure(text = "Australian Shepherd", command = question4_right)
    answer_three.configure(text = "Australian Cattle Dog", command = question4)
    answer_four.configure(text = "Anatolian Shepherd Dog", command = question4)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question3_right():
    image.configure(file= images[2])
    answer_one.configure(text = "American Water Spaniel", command = question4)
    answer_two.configure(text = "Australian Shepherd", command = question4_right)
    answer_three.configure(text = "Australian Cattle Dog", command = question4)
    answer_four.configure(text = "Anatolian Shepherd Dog", command = question4)
    question.configure(text = "Correct! \n What breed is this dog?")

def question4():
    image.configure(file= images[3])
    answer_one.configure(text = "Beagle", command = question5)
    answer_two.configure(text = "Basset Hound", command = question5)
    answer_three.configure(text = "Basenji", command = question5_right)
    answer_four.configure(text = "Australian Terrier", command = question5)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question4_right():
    image.configure(file= images[3])
    answer_one.configure(text = "Beagle", command = question5)
    answer_two.configure(text = "Basset Hound", command = question5)
    answer_three.configure(text = "Basenji", command = question5_right)
    answer_four.configure(text = "Australian Terrier", command = question5)
    question.configure(text = "Correct! \n What breed is this dog?")

def question5():
    image.configure(file= images[4])
    answer_one.configure(text = "Bedlington Terrier", command = question6)
    answer_two.configure(text = "Belgian Malinois", command = question6_right)
    answer_three.configure(text = "Beauceron", command = question6)
    answer_four.configure(text = "Beared Collie", command = question6)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question5_right():
    image.configure(file= images[4])
    answer_one.configure(text = "Bedlington Terrier", command = question6)
    answer_two.configure(text = "Belgian Malinois", command = question6_right)
    answer_three.configure(text = "Beauceron", command = question6)
    answer_four.configure(text = "Beared Collie", command = question6)
    question.configure(text = "Correct! \n What breed is this dog?")

def question6():
    image.configure(file= images[5])
    answer_one.configure(text = "Bernese Mountain Dog", command = question7_right)
    answer_two.configure(text = "Bichon Frise", command = question7)
    answer_three.configure(text = "Belgian Sheepdog", command = question7)
    answer_four.configure(text = "Belgian Tervuren", command = question7)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question6_right():
    image.configure(file= images[5])
    answer_one.configure(text = "Bernese Mountain Dog", command = question7_right)
    answer_two.configure(text = "Bichon Frise", command = question7)
    answer_three.configure(text = "Belgian Sheepdog", command = question7)
    answer_four.configure(text = "Belgian Tervuren", command = question7)
    question.configure(text = "Correct! \n What breed is this dog?")

def question7():
    image.configure(file= images[6])
    answer_one.configure(text = "Black Russian Terrier", command = question8)
    answer_two.configure(text = "Black and Tan Coonhound", command = question8)
    answer_three.configure(text = "Bloodhound", command = question8)
    answer_four.configure(text = "Border Collie", command = question8_right)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question7_right():
    image.configure(file= images[6])
    answer_one.configure(text = "Black Russian Terrier", command = question8)
    answer_two.configure(text = "Black and Tan Coonhound", command = question8)
    answer_three.configure(text = "Bloodhound", command = question8)
    answer_four.configure(text = "Border Collie", command = question8_right)
    question.configure(text = "Correct! \n What breed is this dog?")

def question8():
    image.configure(file= images[7])
    answer_one.configure(text = "Border Terrier", command = question9)
    answer_two.configure(text = "Borzoi", command = question9)
    answer_three.configure(text = "Bouvier des Flandres", command = question9)
    answer_four.configure(text = "Boston Terrier", command = question9_right)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question8_right():
    image.configure(file= images[7])
    answer_one.configure(text = "Border Terrier", command = question9)
    answer_two.configure(text = "Borzoi", command = question9)
    answer_three.configure(text = "Bouvier des Flandres", command = question9)
    answer_four.configure(text = "Boston Terrier", command = question9_right)
    question.configure(text = "Correct! \n What breed is this dog?")

def question9():
    image.configure(file= images[8])
    answer_one.configure(text = "Boxer", command = question10)
    answer_two.configure(text = "Brittany", command = question10)
    answer_three.configure(text = "Brussels Griffon", command = question10)
    answer_four.configure(text = "Briard", command = question10_right)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question9_right():
    image.configure(file= images[8])
    answer_one.configure(text = "Boxer", command = question10)
    answer_two.configure(text = "Brittany", command = question10)
    answer_three.configure(text = "Brussels Griffon", command = question10)
    answer_four.configure(text = "Briard", command = question10_right)
    question.configure(text = "Correct! \n What breed is this dog?")

def question10():
    image.configure(file= images[9])
    answer_one.configure(text = "Bulldog", command = final)
    answer_two.configure(text = "Bullmastiff", command = final_right)
    answer_three.configure(text = "Cairn Terrier", command = final)
    answer_four.configure(text = "Bull Terrier", command = final)
    question.configure(text = "Incorrect! \n What breed is this dog?")

def question10_right():
    image.configure(file= images[9])
    answer_one.configure(text = "Bulldog", command = final)
    answer_two.configure(text = "Bullmastiff", command = final_right)
    answer_three.configure(text = "Cairn Terrier", command = final)
    answer_four.configure(text = "Bull Terrier", command = final)
    question.configure(text = "Correct! \n What breed is this dog?")

def final():
    image.configure(file= images[10])
    answer_one.configure(text = " ")
    answer_two.configure(text = " ")
    answer_three.configure(text = " ")
    answer_four.configure(text = " ")
    question.configure(text = "Incorrect! \n Thank you for playing!")

def final_right():
    image.configure(file= images[10])
    answer_one.configure(text = " ")
    answer_two.configure(text = " ")
    answer_three.configure(text = " ")
    answer_four.configure(text = " ")
    question.configure(text = "Correct! \n Thank you for playing!")

answer_one = tk.Button(text = "Affenpinscher",font = ("Avenir"), command = question2)
tk.Button
answer_one.pack()

answer_two = tk.Button(text = "Airedale Terrier",font = ("Avenir"), command = question2)
tk.Button
answer_two.pack()

answer_three = tk.Button(text = "Akita",font = ("Avenir"), command = question2)
tk.Button
answer_three.pack()

answer_four = tk.Button(text = "Afghan Hound",font = ("Avenir"), command = question2_right)
tk.Button
answer_four.pack()



root.mainloop()
