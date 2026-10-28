"""
Tally Counter
Given a string of tally marks, return the total count represented.

- Each pipe "|" represents one count.
- Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
- Groups are separated by a space.

1. getTallyCount("||||") should return 4.
2. getTallyCount("||||/") should return 5.
3. getTallyCount("||||/ |||") should return 8.
4. getTallyCount("||||/ ||||/ ||||/ ||") should return 17.
5. getTallyCount("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |") should return 41.
"""

def get_tally_count(s: str) -> int:
    tally_list: list[str] = s.split()

    return (len(tally_list) - 1) * 5 + len(tally_list[-1])


print(get_tally_count("||||"))
print(get_tally_count("||||/"))
print(get_tally_count("||||/ |||"))
print(get_tally_count("||||/ ||||/ ||||/ ||"))
print(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"))
