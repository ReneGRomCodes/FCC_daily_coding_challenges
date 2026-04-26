"""
FizzBuzz Explosion

Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given
number of "z"'s using the following rules:
- Start with the string "fizzbuzz".
- Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
    - If the letter position is divisible by 3, replace the letter with "fizz"
    - If it's divisible by 5, replace the letter with "buzz"
    - If it's divisible by 3 and 5, replace the letter with "fizzbuzz"

So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.

1. explodeFizzbuzz(9) should return 1.
2. explodeFizzbuzz(15) should return 2.
3. explodeFizzbuzz(51) should return 3.
4. explodeFizzbuzz(52) should return 4.
5. explodeFizzbuzz(359) should return 5.
6. explodeFizzbuzz(789) should return 6.
7. explodeFizzbuzz(54482) should return 11.
8. explodeFizzbuzz(1000000) should return 14.
"""

def explode_fizzbuzz(target_z_count: int) -> int:
    start_fb: str = "fizzbuzz"
    exploded_fizzbuzz: list[str] = []
    steps: int = 0

    while True:
        for pos, char in enumerate(start_fb, start=1):
            is_fizz: bool = pos % 3 == 0
            is_buzz: bool = pos % 5 == 0
            is_fizzbuzz: bool = is_fizz and is_buzz

            if is_fizzbuzz:
                exploded_fizzbuzz.append("fizzbuzz")
            elif is_fizz:
                exploded_fizzbuzz.append("fizz")
            elif is_buzz:
                exploded_fizzbuzz.append("buzz")
            else:
                exploded_fizzbuzz.append(char)

        steps += 1
        exploded_fizzbuzz_str: str = "".join(exploded_fizzbuzz)

        if exploded_fizzbuzz_str.count("z") >= target_z_count:
            return steps

        start_fb = exploded_fizzbuzz_str
        exploded_fizzbuzz = []


print(explode_fizzbuzz(9))
print(explode_fizzbuzz(15))
print(explode_fizzbuzz(51))
print(explode_fizzbuzz(52))
print(explode_fizzbuzz(359))
print(explode_fizzbuzz(789))
print(explode_fizzbuzz(54482))
print(explode_fizzbuzz(1000000))
