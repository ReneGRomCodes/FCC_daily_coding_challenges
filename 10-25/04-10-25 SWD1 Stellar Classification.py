"""
Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar
classification based on the following ranges:
"O": 30,000 K or higher
"B": 10,000 K - 29,999 K
"A": 7,500 K - 9,999 K
"F": 6,000 K - 7,499 K
"G": 5,200 K - 5,999 K
"K": 3,700 K - 5,199 K
"M": 0 K - 3,699 K

Return the classification of the given star.
1. classification(5778) should return "G".
2. classification(2400) should return "M".
3. classification(9999) should return "A".
4. classification(3700) should return "K".
5. classification(3699) should return "M".
6. classification(210000) should return "O".
7. classification(6000) should return "F".
8. classification(11432) should return "B".
"""

# Array with 'threshold temperature - classification' pairs.
CLASSES: list[tuple[int, str]] = [
    (30000, "O"),
    (10000, "B"),
    (7500,  "A"),
    (6000,  "F"),
    (5200,  "G"),
    (3700,  "K"),
    (0,     "M")
]


def classification(temp: int) -> str:

    for threshold, label in CLASSES:
        if temp >= threshold:
            return label

    return "Psst... temperatures can't be negative in Kelvin."


print(classification(5778))
print(classification(2400))
print(classification(9999))
print(classification(3700))
print(classification(3699))
print(classification(210000))
print(classification(6000))
print(classification(11432))
