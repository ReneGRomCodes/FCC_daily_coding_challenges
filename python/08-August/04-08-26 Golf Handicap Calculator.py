"""
Golf Handicap Calculator

Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using
the following method:
- Calculate the differential for each round by subtracting the par from the score, then return the average of all
  differentials rounded to one decimal place.

1. calculate_handicap([72, 72, 72], [72, 72, 72]) should return 0.
2. calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]) should return 6.
3. calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]) should return 8.3.
4. calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]) should return 8.8.
5. calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]) should return 11.7.
"""

def calculate_handicap(scores: list[int], pars: list[int]) -> int | float:
    differentials: list[int] = [score - par for score, par in zip(scores, pars)]
    rounded_sum = int((sum(differentials) / len(differentials)) * 10 + 0.5) / 10

    return rounded_sum if rounded_sum % 1 != 0 else int(rounded_sum)


print(calculate_handicap([72, 72, 72], [72, 72, 72]))
print(calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]))
print(calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]))
print(calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]))
print(calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]))
