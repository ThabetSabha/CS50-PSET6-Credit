cardNumber = (input("Number: "))

i = len(cardNumber) - 2
j = len(cardNumber) - 1

first = []
second = []

while i >= 0 or j >= 0:
    if i >= 0:
        elem = int(cardNumber[i]) * 2
        if elem >= 10:
            first.append(1)
            first.append(elem % 10)
        else:
            first.append(elem)
    if j >= 0:
        second.append(int(cardNumber[j]))
    i -= 2
    j -= 2

sumOfNumbers = sum(first) + sum(second)
firstTwoNumber = cardNumber[0] + cardNumber[1]

if sumOfNumbers % 10 != 0:
    print("INVALID")
elif firstTwoNumber == "34" or firstTwoNumber == "37":
    print("AMEX")
elif cardNumber[0] == "4":
    print("VISA")
else:
    print("MASTERCARD")
