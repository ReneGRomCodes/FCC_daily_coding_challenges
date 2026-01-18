"""
BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is
correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.

1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
2. is_fizz_buzz([1, 2, 3, 4]) should return False.
3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
4. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) should return False.
5. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) should return False.
6. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) should return False.
7. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz",
    19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37,
    38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) should return True.
"""

# Copied over this function from the solution for yesterday's challenge.
def fizz_buzz(n: int) -> list[int | str]:
    fizzbuzz: list[int | str] = []

    for i in range(1, n+1):
        fizz: bool = i % 3 == 0
        buzz: bool = i % 5 == 0

        if fizz and buzz:
            fizzbuzz.append("FizzBuzz")
            continue
        elif fizz:
            fizzbuzz.append("Fizz")
            continue
        elif buzz:
            fizzbuzz.append("Buzz")
            continue
        else:
            fizzbuzz.append(i)

    return fizzbuzz


def is_fizz_buzz(sequence: list[int | str]) -> bool:
    return sequence == fizz_buzz(len(sequence))


print(is_fizz_buzz([1, 2, "Fizz", 4]))
print(is_fizz_buzz([1, 2, 3, 4]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz",
    19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37,
    38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))
