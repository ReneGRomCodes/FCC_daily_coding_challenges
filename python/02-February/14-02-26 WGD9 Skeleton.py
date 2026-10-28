"""
2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment

Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200

1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy".
"""

def get_difficulty(track: str) -> str:
    segments: list[str] = [x for x in track]
    points: int = 0

    for i, segment in enumerate(segments):
        has_curve: bool = segment in {"L", "R"}
        has_direction_change: bool = (
                i != 0 and
                (segment == "L" and segments[i - 1] == "R") or
                (segment == "R" and segments[i - 1] == "L")
        )

        if has_direction_change:
            points += 15
        elif has_curve:
            points += 5

    if points <= 100:
        return "Easy"
    elif points <= 200:
        return "Medium"
    else:
        return "Hard"


print(get_difficulty("SLSLLSRRLSRLRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))
