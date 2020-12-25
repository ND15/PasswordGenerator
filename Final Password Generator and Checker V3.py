import random

passList = ""
char = ''


def randNum():
    return random.randint(48, 57)


def randUpAlpha():
    return random.randint(65, 92)


def randLowAlpha():
    return random.randint(97, 123)


def randSpecial():
    return random.randint(34, 39)


def isSpecial(pwlist):
    for x in pwlist:
        if x in '!#$%&':
            return True


def strength(passList):
    len_passList = len(passList)
    count_num = any(char.isdigit() for char in passList)
    count_upper = any(char.isupper() for char in passList)
    count_lower = any(char.islower() for char in passList)
    count_special = isSpecial(passList)

    if len_passList <= 6:
        print("Password strength: Weak")
    elif len_passList <= 10:
        print("Password strength: Medium")
    else:
        if count_upper == True and count_lower == True and count_num == True and count_special == True:
            print("Password strength: Strong")
        else:
            print("Password strength: Medium")


while True:
    print("Welcome to Password Generator and Checker.")
    while True:
        choice = input("\nEnter 1 to generate a password: \nEnter 2 to check the strength of the password:\n")
        if choice in ('1', '2'):
            break
        else:
            print("Invalid Inputs Given.")

    if choice == "1":
        a = int(input("\nEnter the length of the password you want: "))
        for i in range(0, a):

            b = random.randint(0, 3)
            if b == 0:
                value = chr(randNum())
                passList += value

            if b == 1:
                value = chr(randUpAlpha())
                passList += value

            if b == 2:
                value = chr(randLowAlpha())
                passList += value

            if b == 3:
                value = chr(randSpecial())
                passList += value
        print(passList)
        strength(passList)

    elif choice == "2":
        passList = input("\nEnter the password: ")
        strength(passList)

    while True:
        answer = str(input('\nRun again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        passList = ""

        continue
    else:
        print("Goodbye and take care :) ")
        break
