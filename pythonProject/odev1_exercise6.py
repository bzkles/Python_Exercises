#ODEV1
#Exercise6

import math

def cube(number):
    number = 9
    number = pow(number, 3)
    return number

def by_three(number):

    if number % 3 == 0 :
        return cube()
    else:
        return False

if __name__ == "__main__":
   by_three()