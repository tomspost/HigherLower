print "PLay to higher lower get 5 in a row to win!!"
print ""
import random
count  = 1
n1 = random.randint(1, 10)
while count < 6:
    print  ("guesses %i" % count)
    print n1
    n2 = random.randint(1, 10)
    while n1 == n2:
        n2 = random.randint(1, 10)
    # print n2
    guess = raw_input("guess h/l? ")
    if guess == "h":
        if n2 > n1:
            print "\033[92mcorrect"
        else:
            print "\033[91mwrong"
            count = 0
    else:
        if n1 > n2:
            print "\033[92mcorrect"
        else:
            print "\033[91mwrong"
            count = 0
    count = count + 1
    n1 = n2
    print ""
print "You win !!!"
