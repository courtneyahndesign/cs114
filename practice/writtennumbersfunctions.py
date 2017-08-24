#function version

print("Give me a one to two digit number and I'll write it out for you! (Ex: 34, thirty four)")
number = input()

tens = int(number) //10
ones = int(number) % 10

def calculate_tens(tens):
    if tens == 0:
        tens_number = ""
    if tens == 1:
        tens_number = ""
    if tens == 2:
        tens_number = " twenty"
    elif tens == 3:
        tens_number = " thirty"
    elif tens == 4:
        tens_number = " forty"
    elif tens == 5:
        tens_number = " fifty"
    elif tens == 6:
        tens_number = " sixty"
    elif tens == 7:
        tens_number = " seventy"
    elif tens == 8:
        tens_number = " eighty"
    elif tens == 9:
        tens_number = " ninety"
    return tens_number

def calculate_ones(ones,tens):
    if ones == 1:
        if tens == 1:
            ones_number = "eleven"
        else:
            ones_number = "one"
    elif ones == 0:
        if tens == 1:
            ones_number = "ten"
    elif ones == 2:
        if tens == 1:
            ones_number = "twelve"
        else:
            ones_number = "two"
    elif ones == 3:
        if tens == 1:
            ones_number = "thirteen"
        else:
            ones_number = "three"
    elif ones == 4:
        if tens == 1:
            ones_number = "fourteen"
        else:
            ones_number = "four"
    elif ones == 5:
        if tens == 1:
            ones_number = "fifteen"
        else:
            ones_number = "five"
    elif ones == 6:
        if tens == 1:
            ones_number = "sixteen"
        else:
            ones_number = "six"
    elif ones == 7:
        if tens == 1:
            ones_number = "seventeen"
        else:
            ones_number = "seven"
    elif ones == 8:
        if tens == 1:
            ones_number = "eighteen"
        else:
            ones_number = "eight"
    elif ones == 9:
        if tens == 1:
            ones_number = "nineteen"
        else:
            ones_number = "nine"
    return ones_number

def main():
    tens_final = calculate_tens(tens)
    ones_final = calculate_ones(ones,tens)
    result = "Your number is" + str(tens_final) + " " + str(ones_final)
    return print(result)


main()


# def main():
#     tens_final = calculate_tens()
#     ones_final = calculate_ones()
#     phrase = tens_final + ones_final
#     return print(phrase)
#
# main()
