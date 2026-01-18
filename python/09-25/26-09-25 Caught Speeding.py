"""
Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing
the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average
amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].

1. speeding([50, 60, 55], 60) should return [0, 0].
2. speeding([58, 50, 60, 55], 55) should return [2, 4].
3. speeding([61, 81, 74, 88, 65, 71, 68], 70) should return [4, 8.5].
4. speeding([100, 105, 95, 102], 100) should return [2, 3.5].
5. speeding([40, 45, 44, 50, 112, 39], 55) should return [1, 57].
"""

def speeding(speeds: list[int], limit: int) -> list[int | float]:
    speeding_cars: list[int] = [x for x in speeds if x > limit]
    n_speeding_cars: int = len(speeding_cars)

    if n_speeding_cars > 0:
        speeds_over_limit: list[int] = [x - limit for x in speeding_cars]
        avrg_over_limit: int | float = sum(speeds_over_limit) / n_speeding_cars

        if avrg_over_limit % 1 == 0:  # Turn '.0' floats into integers.
            avrg_over_limit: int = int(avrg_over_limit)

    else:
        avrg_over_limit: int = 0

    return [n_speeding_cars, avrg_over_limit]


print(speeding([50, 60, 55], 60))
print(speeding([58, 50, 60, 55], 55))
print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))
print(speeding([40, 45, 44, 50, 112, 39], 55))
