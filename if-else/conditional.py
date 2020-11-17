import random

def is_positive(a):
    if (a > 0):
        print('Положительное')
    elif (a < 0):
        print('Отричательное')
    else:
        print('равно нулю')
    # return true if num is positive, otherwise return false

def is_even(a):
    if a%2==0:
        print('четное')
    else:
        print('нечетное')
    # return true if num is even, otherwise return false


def is_positive_and_even(a):
    if a>0 and a%2==0:
        print('true')
    elif a<0:
        print('false')
    else:
        print('равно нулю')
    # return true if num is positive and even, otherwise return false


def is_positive_or_even(a):
    if a>0 or a%2==0:
        print('true')
    elif a<0:
        print('false')
    else:
        print('equals zero')
    # return true if num is positive or even, otherwise return false

print(is_positive(3))
print(is_even(2))
print(is_positive_and_even(4))
print(is_positive_or_even(0))
