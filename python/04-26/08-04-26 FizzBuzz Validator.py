"""
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

- Multiples of 3 are replaced with "Fizz".
- Multiples of 5 are replaced with "Buzz".
- Multiples of both 3 and 5 are replaced with "FizzBuzz".
- All other numbers remain as integers.

1. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]) should return True.
2. is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]) should return True.
3. is_fizz_buzz([1, 2, "Fizz", 4, 5]) should return False.
4. is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]) should return True.
5. is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]) should return False.
6. is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]) should return False.
7. is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]) should return True.
"""

def get_original_sequence(arr: list[int | str]) -> list[int]:
    """Build and return original integer sequence from passed FizzBuzz sequence.
    ARGS:
        arr: list[int | str] FizzBuzz sequence.
    RETURNS:
        list of integers representing original integer sequence.
    """
    original_sequence: list[int] = []

    for index, value in enumerate(arr):
        if isinstance(value, int):
            original_sequence.append(value - index)
            break

    for _ in range(len(arr) - 1):
        original_sequence.append(original_sequence[-1] + 1)

    return original_sequence


def is_fizz_buzz(arr: list[int | str]) -> bool:
    # 'Reverse engineer' the original integer sequence.
    original_sequence: list[int] = get_original_sequence(arr)

    for val_1, val_2 in zip(original_sequence, arr):
        if val_1 % 15 == 0:
            correct_val = "FizzBuzz"
        elif val_1 % 3 == 0:
            correct_val = "Fizz"
        elif val_1 % 5 == 0:
            correct_val = "Buzz"
        else:
            correct_val = val_1  # Should be integer.

        if val_2 != correct_val:
            return False

    return True


print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))
print(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]))
print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]))
print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]))
print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]))
