#################################################################
# FILE : shapes.py
# WRITER : achikam levy , aaa997 , 208764944
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import math

def shape_area():
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape == '1' or shape == '2' or shape == '3':
        if shape == '1':
            r = input()
            r = float(r)
            circle_area = r**2*math.pi
            return circle_area
        if shape == '2':
            a = input()
            b = input()
            a, b = float(a), float(b)
            rectangle_area = a*b
            return rectangle_area
        if shape == '3':
            a = input()
            a = float(a)
            triangle_area = ((3**0.5)/4)*(a**2)
            return triangle_area
    else:
        return None





#def print_seq(n, m):
    for i in range(1, n+1):
        if i == m:
            print(m, end='!''\n')
        else:
            print(i)

def print_seq(n):
    lst = ()
    for i in range(1, n):
        print(i, end=' ,')
    print(n)


def print_seq(n):
    if n%2 == 1:
        for i in range(1, n-1):
            if i%2 == 1:
                print(i, end=', ')
        print(n)
    else:
        for i in range(1, n-1):
            if i%2 == 1:
                print(i, end=', ')
        print(n-1)

def is_prime_very_fast(n):
    if n == 1:
       return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % 2 == 1:
            if n % i == 0 :
                return False
        elif n % 2 == 0:
            return False
    else:
        return True

def factorial_list(n):
    lst = []
    big_lst = []
    for i in range(1, n+1):
        lst.append(i)
        big_lst.append(lst)
        lst = lst[:]

    return big_lst

def find_biggest(lst):
    x = 0
    sum_lst = 0
    for i in range(len(lst)):
        for r in range(len(lst[i])):
            x = x + lst[i][r]
            sum_lst = x
            if sum_lst < x:
                sum_lst = x
    print(sum_lst)

if __name__ == "__main__":
    print(find_biggest([[1, 2, 3], [10, -2], [1, 1, 1, 1]]))
    #print(factorial_list(4))