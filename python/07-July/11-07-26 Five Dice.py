"""
Five Dice
Given an array of five dice with values 1-6, return the best possible hand.

Here are the hands ranked lowest to highest:

Hand	            Description
"no pair"	        No pair or better
"pair"	            Two dice with the same value
"two pair"	        Two different pairs
"three of a kind"	Three dice with the same value
"small straight"	Four consecutive values
"large straight"	Five consecutive values
"full house"	    Three of a kind and a pair
"four of a kind"	Four dice with the same value
"five of a kind"	All five dice with the same value

1. five_dice([1, 1, 1, 1, 1]) should return "five of a kind".
2. five_dice([5, 5, 5, 6, 5]) should return "four of a kind".
3. five_dice([2, 5, 6, 4, 3]) should return "large straight".
4. five_dice([4, 3, 3, 3, 1]) should return "three of a kind".
5. five_dice([4, 6, 2, 6, 5]) should return "pair".
6. five_dice([1, 4, 5, 6, 2]) should return "no pair".
7. five_dice([1, 3, 4, 6, 2]) should return "small straight".
8. five_dice([2, 2, 5, 2, 5]) should return "full house".
9. five_dice([6, 4, 5, 6, 4]) should return "two pair".
"""

def get_dice_hist(dice: list[int]) -> dict[int, int]:
    """Build and return histogram for 'dice'."""
    dice_hist: dict[int, int] = {}

    for item in dice:
        if item in dice_hist:
            dice_hist[item] += 1
        else:
            dice_hist[item] = 1

    return dice_hist


def five_dice(dice: list[int]) -> str | None:
    sorted_dice: list[int] = sorted(dice)
    dice_hist: dict[int, int] = get_dice_hist(sorted_dice)
    dice_hist_length: int = len(dice_hist)

    # Check for straights first.
    large_straights: tuple[list[int], ...] = ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    small_straights: tuple[set[int], ...] = ({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6})

    if sorted_dice in large_straights:
        return "large straight"

    for straight in small_straights:
        if straight.issubset(dice_hist.keys()):
            return "small straight"

    # Further checks based on length of 'dice_hist_length'.
    if dice_hist_length == 1:
        return "five of a kind"

    elif dice_hist_length == 2:
        if 4 in dice_hist.values():
            return "four of a kind"
        elif 3 in dice_hist.values():
            return "full house"

    elif dice_hist_length == 3:
        if 3 in dice_hist.values():
            return "three of a kind"
        elif 2 in dice_hist.values():
            return "two pair"

    elif dice_hist_length == 4:
        return "pair"

    elif dice_hist_length == 5:
        return "no pair"

    return None


print(five_dice([1, 1, 1, 1, 1]))
print(five_dice([5, 5, 5, 6, 5]))
print(five_dice([2, 5, 6, 4, 3]))
print(five_dice([4, 3, 3, 3, 1]))
print(five_dice([4, 6, 2, 6, 5]))
print(five_dice([1, 4, 5, 6, 2]))
print(five_dice([1, 3, 4, 6, 2]))
print(five_dice([2, 2, 5, 2, 5]))
print(five_dice([6, 4, 5, 6, 4]))
