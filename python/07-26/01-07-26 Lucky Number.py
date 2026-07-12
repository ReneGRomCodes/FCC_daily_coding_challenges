"""
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number

If the final value is zero (0), return 13.

1. get_lucky_number("John Doe") should return 21.
2. get_lucky_number("Olivia Lewis") should return 52.
3. get_lucky_number("James Wilson") should return 18.
4. get_lucky_number("Elizabeth Hernandez") should return 81.
5. get_lucky_number("Mike Walker") should return 32.
6. get_lucky_number("Chloe Perez") should return 13.
"""

def get_vowel_consonant_count(s: str) -> tuple[int, int]:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    vowel_count, consonant_count = 0, 0

    for char in s.lower():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count


def get_lucky_number(name: str) -> int:
    first_name, last_name = name.split()
    fn_vowel_count, fn_consonant_count = get_vowel_consonant_count(first_name)
    ln_vowel_count, ln_consonant_count = get_vowel_consonant_count(last_name)

    # Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name.
    smaller_val = (min(fn_vowel_count, ln_vowel_count) * min(fn_consonant_count, ln_consonant_count) *
                   min(len(first_name), len(last_name)))

    # Do the same for the two larger counts and the larger name.
    larger_val = (max(fn_vowel_count, ln_vowel_count) * max(fn_consonant_count, ln_consonant_count) *
                  max(len(first_name), len(last_name)))

    lucky_number = larger_val - smaller_val

    return 13 if lucky_number == 0 else lucky_number


print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))
