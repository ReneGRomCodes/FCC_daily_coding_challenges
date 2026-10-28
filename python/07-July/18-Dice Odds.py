"""
Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format
"1 in X".

- The number of dice will be between 1 and 6.
- The target sum is always achievable with the given number of dice.
- Round "X" to the nearest whole number.

1. get_odds(1, 5) should return "1 in 6".
2. get_odds(2, 4) should return "1 in 12".
3. get_odds(3, 10) should return "1 in 8".
4. get_odds(4, 7) should return "1 in 65".
5. get_odds(5, 26) should return "1 in 111".
6. get_odds(6, 35) should return "1 in 7776".
"""

def get_odds(dice: int, target: int) -> str:
    ways = [0] * 37
    ways[0] = 1

    for _ in range(dice):
        next_ways = [0] * 37

        for current_sum in range(37):
            if ways[current_sum] > 0:

                for face in range(1, 7):
                    if current_sum + face <= 36:
                        next_ways[current_sum + face] += ways[current_sum]
        ways = next_ways

    total_outcomes = 6 ** dice
    ways_to_win = ways[target]
    x = round(total_outcomes / ways_to_win)

    return f"1 in {x}"


print(get_odds(1, 5))
print(get_odds(2, 4))
print(get_odds(3, 10))
print(get_odds(4, 7))
print(get_odds(5, 26))
print(get_odds(6, 35))
