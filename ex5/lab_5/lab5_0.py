
def fizzBuzz_1(num: int) -> str or int:
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    else:
        return num
