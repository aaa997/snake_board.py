
#################################################################
# FILE : math_print.py
# WRITER : your_name , your_login , your_id
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################
import math

def golden_ratio():
    """
      this print the golden_ratio
      :return: None
      """
    print((1 + 5 ** 0.5) / 2)


def six_squared():
    """
        this print the six_squared of 6**2
        :return: None
        """
    print(6 ** 2)


def hypotenuse():
    """
           this print the hypotenuse of triangle 5*12
           :return: None
           """
    print(math.hypot(12 ,5))


def pi():
    """
               this print the value of pi
               :return: None
               """
    print(math.pi)


def e():
    """
                   this print the value of pi
                   :return: None
                   """
    print(math.exp(1))


def squares_area():
    """
                       this print the value of the squares_area in range 1-10
                       :return: None
                       """

    print(1 * 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5, 6 * 6, 7 * 7, 8 * 8,
          9 * 9, 10 * 10)


if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
