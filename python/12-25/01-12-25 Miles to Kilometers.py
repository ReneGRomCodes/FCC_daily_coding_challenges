"""
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.

1. convert_to_km(1) should return 1.61.
2. convert_to_km(21) should return 33.8.
3. convert_to_km(3.5) should return 5.63.
4. convert_to_km(0) should return 0.
5. convert_to_km(0.621371) should return 1.
"""

def convert_to_km(miles: int | float) -> int | float:
    kilometers = round(miles * 1.60934, 2)

    if kilometers % 1 == 0:
        return int(kilometers)

    return kilometers


print(convert_to_km(1))
print(convert_to_km(21))
print(convert_to_km(3.5))
print(convert_to_km(0))
print(convert_to_km(0.621371))
