"""
Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	     Base Value
"bottle"	    10
"can"	         6
"bag"	         8
"tire"	        35
"straw"	         4
"cardboard"	     3
"newspaper"	     3
"shoe"	        12
"electronics"	25
"battery"	    18
"mattress"	    38

A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

- Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
    - First consecutive occurrence: base value
    - Second: base value + 1
    - Third: base value + 2
    - etc.

- Fifth Item Multiplier: Every fifth item collected gets a multiplier.
    - Fifth item: *2
    - Tenth item: *3
    - etc.

Apply the multiplier after calculating any bonuses.

1. get_cleanup_score(["bottle", "straw", "shoe", "battery"]) should return 44.
2. get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) should return 58.
3. get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]) should return 79.
4. get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) should return 358.
5. get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can",
    "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"])
        should return 383.
"""

def get_cleanup_score(items: list) -> int:
    item_scores: dict[str, int] = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38,
    }
    streak_count: int = 1
    score: int = 0

    for pos, item in enumerate(items, start=1):
        is_normal_item: bool = type(item) == str and item in item_scores
        is_rare_item: bool = type(item) == list and item[0] == "rare" and type(item[1]) == int
        is_streak: bool = pos > 1 and items[pos - 2] == item and not is_rare_item
        apply_fifth_item_multiplier: bool = pos % 5 == 0

        item_score: int = 0

        if is_normal_item:
            item_score += item_scores[item]
        elif is_rare_item:
            item_score += item[1]
        else:
            continue  # Skip invalid items.

        if is_streak:
            item_score += streak_count
            streak_count += 1
        elif streak_count != 1:  # Reset streak count if streak is broken.
            streak_count = 1

        if apply_fifth_item_multiplier:
            item_score *= pos / 5 + 1

        score += int(item_score)

    return score


print(get_cleanup_score(["bottle", "straw", "shoe", "battery"]))
print(get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]))
print(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))
print(get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]))
print(get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can",
                         "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can",
                         "can"]))
