"""
Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.

The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional
stops can be placed anywhere in the itinerary, subject to the following rules:

- "breakfast" is always first, with at least one stop before "lunch".
- "lunch" must appear before "dinner", with at least one stop in between.
- At most, one optional stop may appear after "dinner".

Return the number of valid arrangements.

1. get_itinerary_count(["library", "park"]) should return 2.
2. get_itinerary_count(["library", "park", "arcade"]) should return 18.
3. get_itinerary_count(["library", "park", "arcade", "store"]) should return 120.
4. get_itinerary_count(["library", "park", "arcade", "store", "cafe"]) should return 840.
5. get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]) should return 55440.
"""

import math

def get_itinerary_count(stops: list[str]) -> int:
    return (2 * len(stops) - 3) * math.factorial(len(stops))


print(get_itinerary_count(["library", "park"]))
print(get_itinerary_count(["library", "park", "arcade"]))
print(get_itinerary_count(["library", "park", "arcade", "store"]))
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe"]))
print(get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]))
