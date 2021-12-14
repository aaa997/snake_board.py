#################################################################
# FILE : quadratic_equation.py
# WRITER : achikam levy , aaa997 , 208764944
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import math


def quadratic_equation(x,y,z):
    in_sqrt = y**2-4*x*z
    if in_sqrt < 0 or x == 0:
        return (None, None)
    outcome_1 = (-y+(math.sqrt(in_sqrt)))/2*x
    outcome_2 = (-y-(math.sqrt(in_sqrt)))/2*x
    if int(outcome_1) == outcome_1:
        outcome_1 = int(outcome_1)
    if int(outcome_2) == outcome_2:
        outcome_2 = int(outcome_2)
    if in_sqrt == 0:
        return (outcome_1, None)
    else:
        return (outcome_1, outcome_2)


def quadratic_equation_user_input():
    a, b, c = input("Insert coefficients a, b, and c: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    outcome_1, outcome_2 = quadratic_equation(a,b,c)
    if type(outcome_1) == int :
        outcome_1 = float(outcome_1)
    if type(outcome_2) == int:
        outcome_2 = float(outcome_2)
    if a == 0:
        print("The parameter 'a' may not equal 0")
    elif quadratic_equation(a,b,c) == (None, None):
        print('The equation has no solutions')
    elif quadratic_equation(a,b,c) == (outcome_1,None):
        print('The equation has 1 solution:',outcome_1)
    else:
        print('The equation has 2 solutions:',outcome_1,'and',outcome_2)





#if __name__ == "__main__":
   # print(quadratic_equation(1,1.5,-1))


 #   print("Insert coefficients a, b, and c: ")

  #  (quadratic_equation_user_input())

