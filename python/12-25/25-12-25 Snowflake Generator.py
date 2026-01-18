"""
Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each
line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

*
 *
*
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 **
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

1. generate_snowflake("* \n *\n* ") should return "*  *\n ** \n*  *".
2. generate_snowflake("X=~") should return "X=~~=X".
3. generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ") should return " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ".
4. generate_snowflake("*   *\n * * \n* * *\n * * \n*   *")
    should return "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *".
5. generate_snowflake("*  -\n * -\n*  -") should return "*  --  *\n * -- * \n*  --  *".
"""

def generate_snowflake(crystals: str) -> str:
    crystals_list: list[str] = crystals.split("\n")
    rev_crystals: list[str] = [x[-1::-1] for x in crystals_list]
    snowflake: str = ""

    for index, (a, b) in enumerate(zip(crystals_list, rev_crystals)):
        if index != len(crystals_list) - 1:
            snowflake += f"{a}{b}\n"
        else:
            snowflake += f"{a}{b}"

    return snowflake


print(generate_snowflake("* \n *\n* "))
print(generate_snowflake("X=~"))
print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
print(generate_snowflake("*  -\n * -\n*  -"))
