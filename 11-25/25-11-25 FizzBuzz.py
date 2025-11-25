"""
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".

1. fizz_buzz(2) should return [1, 2].
2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
4. fizz_buzz(20) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"].
5. fizz_buzz(50)
    should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz",
    19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37,
    38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"].
"""

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


print(fizz_buzz(2))
print(fizz_buzz(4))
print(fizz_buzz(8))
print(fizz_buzz(20))
print(fizz_buzz(50))
