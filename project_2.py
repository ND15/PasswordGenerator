import random

passList = []


def ranInt(x, y):
    return random.randint(x, y)


def randNum():
    return random.randint(1, 9)


def randUpAlpha():
    return random.randint(65, 92)


def randLowAlpha():
    return random.randint(97, 123)


def randSpecial():
    return random.randint(34, 39)


a = int(input("Enter the length of the password you want: "))
for i in range(0, a):

    b = ranInt(0, 6)
    if b == 0:
        value = randNum()
        passList.append(value)

    if b == 1:
        value = chr(randSpecial())
        passList.append(value)

    if b == 2:
        value = chr(randUpAlpha())
        passList.append(value)

    if b == 3:
        value = randNum()
        passList.append(value)

    if b == 4:
        value = chr(randSpecial())
        passList.append(value)

    if b == 5:
        value = chr(randLowAlpha())
        passList.append(value)

passList1 = str(passList)

password = " "
for i in passList1:
    password += i

print(password)




