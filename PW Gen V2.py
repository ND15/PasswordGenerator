import random

passList = ""
count_num = 0
count_upper = 0
count_lower = 0
count_special = 0


def randNum():
    return random.randint(48, 57)


def randUpAlpha():
    return random.randint(65, 92)


def randLowAlpha():
    return random.randint(97, 123)


def randSpecial():
    spcl = '!@#$%^&*'
    return random.choice(spcl)


def strength(passList):
    len_passList = len(passList)

    if len_passList <= 6:
        print("Password strength: Weak")
    elif len_passList <= 10:
        print("Password strength: Medium")
    else:
        if count_upper > 0 and count_lower > 0 and count_num > 0 and count_special > 0:
            print("Password strength: Strong")
        else:
            print("Password strength: Medium")


while True:
    choice = int(input("\nEnter 1 to generate a password: \nEnter 2 to check the strength of the password:\n"))
    if choice == 1:
        a = int(input("\nEnter the length of the password you want: "))
        for i in range(0, a):

            b = random.randint(0, 3)
            if b == 0:
                count_num += 1
                value = chr(randNum())
                passList += value

            if b == 1:
                count_upper += 1
                value = chr(randUpAlpha())
                passList += value

            if b == 2:
                count_lower += 1
                value = chr(randLowAlpha())
                passList += value

            if b == 3:
                count_special += 1
                value = randSpecial()
                passList += value

        print(passList)
        strength(passList)

    elif choice == 2:
        passList = input("\nEnter the password: ")
        strength(passList)

    while True:
        answer = str(input('\nRun again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        count_num = 0
        count_upper = 0
        count_lower = 0
        count_special = 0
        passList = ""

        continue
    else:
        print("Goodbye and take care :) ")
        break
