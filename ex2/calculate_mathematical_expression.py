#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : achikam levy , aaa997 , 208764944
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def calculate_mathematical_expression(x,y,z):
    if z in ('+','-',':','*' ):
        if y != 0 :
            if z == '+':
                outcome = x+y
            elif z == '-':
                outcome = x-y
            elif z == ':':
                outcome = x/y
            elif z == '*':
                outcome = x*y
            return(outcome)
    return None



def calculate_from_string(cal_string):
    x1 , z , y1 = cal_string.split()
    x = float(x1)
    y = float(y1)
    outcome = calculate_mathematical_expression(x, y, z)
    return(outcome)

#if __name__ == "__main__" :

    #print(calculate_mathematical_expression(6,5,'+'))