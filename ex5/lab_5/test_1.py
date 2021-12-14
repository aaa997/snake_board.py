from lab5_0 import*

def test_fizzBuzz_1():
    assert fizzBuzz_1(3) == "Fizz"
    assert fizzBuzz_1(5) == "Buzz"
    assert fizzBuzz_1(300) == "FizzBuzz"
    assert fizzBuzz_1(4) == 4
    assert fizzBuzz_1(100) == "Buzz"