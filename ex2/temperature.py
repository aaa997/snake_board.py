#################################################################
# FILE : temperature.py
# WRITER : achikam levy , aaa997 , 208764944
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################



def is_vormir_safe(temp_max,day1,day2,day3):
    """this function return bool value if two days were warmer
    then the temp_ max"""
    if day1 >= day2 and day2 > temp_max:
        return True
    if day2 >= day3 and day3 > temp_max:
        return True
    if day3 >= day1 and day1 > temp_max:
        return True
    if day3 >= day2 and day2 > temp_max:
        return True
    else:
        return False




#if __name__ == "__main__":
 #    print(is_vormir_safe(19,12,45,12))