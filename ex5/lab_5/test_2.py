from lab5_1 import*


def test_fizz_Buzz_2():
    assert fizzBuzz_2(3), fizzBuzz_2(23) == "Fizz"
    assert fizzBuzz_2(5), fizzBuzz_2(52) == "Buzz"
    assert fizzBuzz_2(300), fizzBuzz_2(513) == "FizzBuzz"
    assert fizzBuzz_2(4) == 4

