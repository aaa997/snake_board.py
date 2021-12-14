

def fizzBuzz_3(num: int) -> str or int:
    if ('3' in str(num) and num % 3 == 0) and ('5' in str(num) and num % 5 == 0):
        return num
    elif ('3' in str(num) or num % 3 == 0) and ('5' in str(num) or num % 5 == 0):
        return 'FizzBuzz'
    elif '3' in str(num) and num % 3 == 0:
        return num
    elif '5' in str(num) and num % 5 == 0:
        return num
    elif '3' in str(num) or num % 3 == 0:
        return 'Fizz'
    elif '5' in str(num) or num % 5 == 0:
        return 'Buzz'
    else:
        return num


