

def fizzBuzz_2(num: int) -> str or int:
    if ('3' in str(num) or num % 3 == 0) and ('5' in num or num % 5 == 0):
        return 'FizzBuzz'
    if '3' in str(num) or num % 3 == 0:
        return 'Fizz'
    if '5' in str(num) or num % 5 == 0:
        return 'Buzz'
    else:
        return num