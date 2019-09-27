print("")
print("--==| HIGHER LOWER GAME |==--")
print("To win you need get 5 correct gesses")
print("")

import random

number1 = random.randint(1, 10)

count = 1
while count < 6:
    print("================================")
    print("Guess %i number = %i" % (count, number1))
    count += 1
    print("is the next number higher or lower?")
    guess = raw_input("enter h or l?: ")
    number2 = random.randint(1, 10)
    print ("It was %i" % number2)
    if guess == "l":
        if number1 > number2:
            print "CORRECT"
        else:
            print "WRONG"
            count = 1
    else:
        if number1 < number2:
            print "CORRECT"
        else:
            print "WRONG"
            count = 1
    number1 = number2

print("You WIN!!!!")