#Create a program that asks for a number in base-10 that's between 1 and 99 then prints out the name of it in English.

print("Give me a one to two digit number and I'll write it out for you! (Ex: 34, thirty four)")
number = input()

tens = int(number) //10
ones = int(number) % 10

if tens == 2:
    print("twenty ")
elif tens == 3:
    print("thirty ")
elif tens == 4:
    print("forty ")
elif tens == 5:
    print("fifty ")
elif tens == 6:
    print("sixty ")
elif tens == 7:
    print("seventy ")
elif tens == 8:
    print("eighty ")
elif tens == 9:
    print("ninety ")

if ones == 1:
    if tens == 1:
        print("eleven")
    else:
        print("one")
elif ones == 2:
    if tens == 1:
        print("twelve")
    else:
        print("two")
elif ones == 3:
    if tens == 1:
        print("thirteen")
    else:
        print("three")
elif ones == 4:
    if tens == 1:
        print("fourteen")
    else:
        print("four")
elif ones == 5:
    if tens == 1:
        print("fifteen")
    else:
        print("five")
elif ones == 6:
    if tens == 1:
        print("sixteen")
    else:
        print("six")
elif ones == 7:
    if tens == 1:
        print("seventeen")
    else:
        print("seven")
elif ones == 8:
    if tens == 1:
        print("eighteen")
    else:
        print("eight")
elif ones == 9:
    if tens == 1:
        print("nineteen")
    else:
        print("nine")
