from lab5_2 import*

def test_fizzbuzz_3():
    assert fizzBuzz_3(3) == 3
    assert fizzBuzz_3(25) == 25
    assert fizzBuzz_3(13) == "Fizz"
    assert fizzBuzz_3(7) == 7
    assert fizzBuzz_3(351) == "FizzBuzz"
    assert fizzBuzz_3(135) == 135