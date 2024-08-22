# make a function that randomly generates numbers between 1-100 and stop when it outputs 5
from random import randint
def random():
    for i in range(10000):
        i = randint(1,101)
        print(i)
        if i == 5:
            break

def rwhile():
    i = 0
    while i != 5:
        i = randint(1,101)
        print(i)


# same function but also return number of times each number was printed
from collections import Counter
def rwhile():
    i = 0
    hash = {}
    while i != 5:
        i = randint(1,101)
        
        print(i)

rwhile()