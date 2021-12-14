# i choose (0.5,0,3.7) to chek how the function deals with fraction values
# i choose (0,-2 ,-1) to chek how the function deals with negative values


#################################################################
# FILE : largest_and_smallest.py
# WRITER : achikam levy , aaa997 , 208764944
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def largest_and_smallest(x,y,z):
    if x >= y and x >= z:
        largest = x
        if y < z:
            smallest = y
        else:
             smallest = z
        return (largest, smallest)
    elif z >= y and z >= x :
        largest = z
        if y<x:
            smallest = y
        else:
            smallest = x
        return (largest, smallest)
    elif y >= z and y >= x :
        largest = y
        if z<x:
            smallest = z
        else:
            smallest = x
        return (largest, smallest)


def check_largest_and_smallest():
    if ((largest_and_smallest(17,1,6)) == (17, 1) and
    (largest_and_smallest(1,17,6)) == (17, 1) and
    (largest_and_smallest(1,1,2)) == (2, 1) and
    (largest_and_smallest(0.5,-2,3.7)) == (3.7, -2) and
    (largest_and_smallest(0,-2 ,-1)) == (0,-2)):
        return True
    else:
        return False

#if __name__ == "__main__":

   # print(largest_and_smallest(1,5,10))
    #print(check_largest_and_smallest())