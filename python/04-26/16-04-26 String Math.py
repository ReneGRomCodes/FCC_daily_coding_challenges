"""
String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters
between the numbers.

- If the count of characters separating two numbers is even, use addition.
- If it's odd, use subtraction.
- Consecutive digits form a single number.
- Operations are applied left to right.
- Ignore leading and trailing characters that aren't digits.

For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them.
Then subtract 8 from 13 because there's an odd number of characters between the result and 8.

1. do_math("3ab10c8") should return 5.
2. do_math("6MINUS4") should return 2.
3. do_math("9plus3") should return 12.
4. do_math("5fkwo#10i#%.<>15P=@20!#B/25") should return 15.
5. do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt") should return 67.
"""

def split_s_to_numeric(s: str) -> list[str]:
    """Take string 's', splits numeric from non-numeric sections and return them in list of strings.
    ARGS:
        s: str
    RETURN:
        s_split: list of strings containing distinct numeric and non-numeric sections.
    """
    s_split: list[str] = []
    section: str = ""

    for index, char in enumerate(s):
        # Find first numeric character and add to 'section'.
        is_numeric: bool = char.isnumeric()

        if not section:
            if char.isnumeric():
                section += char
            else:
                continue

        # Split numeric from non-numeric characters by checking if current char is of same type as previous char in
        # 'section'. Add 'section' to 's_split' if not and start new 'section' variable.
        else:
            is_previous_numeric: bool = section[-1].isnumeric()

            if (is_numeric and not is_previous_numeric) or (not is_numeric and is_previous_numeric):
                s_split.append(section)
                section = char
            else:
                section += char

        # Ensure last section is only added if it is numeric.
        if index == len(s) - 1 and is_numeric:
            s_split.append(section)

    return s_split


def do_math(s: str) -> int:
    s_split: list[str] = split_s_to_numeric(s)
    sum_n: int = int(s_split[0])

    for index, section in enumerate(s_split):
        # Odd indices (except [0]) indicate operator sections.
        is_operator: bool = index % 2 != 0 and index != 0

        if is_operator:
            # Addition.
            if len(section) % 2 == 0:
                sum_n += int(s_split[index + 1])
            # Subtraction.
            else:
                sum_n -= int(s_split[index + 1])

    return sum_n


print(do_math("3ab10c8"))
print(do_math("6MINUS4"))
print(do_math("9plus3"))
print(do_math("5fkwo#10i#%.<>15P=@20!#B/25"))
print(do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"))
