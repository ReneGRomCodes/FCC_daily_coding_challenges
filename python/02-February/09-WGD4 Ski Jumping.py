"""
2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the
ski jump and determine if you won a medal or not.

Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:

165.5
172.0
158.0
180.0
169.5
175.0
162.0
170.0

If your score is the best, return "Gold"
If it's second best, return "Silver"
If it's third best, return "Bronze"
Otherwise, return "No Medal"

1. ski_jump_medal(125.0, 58.0, 0.0, 6.0) should return "Gold".
2. ski_jump_medal(119.0, 50.0, 1.0, 4.0) should return "Bronze".
3. ski_jump_medal(122.0, 52.0, -1.0, 4.0) should return "Silver".
4. ski_jump_medal(118.0, 50.5, -1.5, 4.0) should return "No Medal".
5. ski_jump_medal(124.0, 50.5, 2.0, 5.0) should return "Gold".
6. ski_jump_medal(119.0, 49.5, 0.0, 3.0) should return "No Medal".
"""

def ski_jump_medal(distance_points: float, style_points: float, wind_comp: float, k_point_bonus: float) -> str:
    """Yeah I know, this is a hilariously overengineered but still wonky solution. I was bored and wanted to try
    something stupid ;) the proper solution is further down."""
    total_score: float = sum([distance_points, style_points, wind_comp, k_point_bonus])
    top_three_scores: list[float] = sorted([165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0, total_score],
                                           reverse=True)[:3]

    if total_score in set(top_three_scores):
        for index, score in enumerate(top_three_scores):
            if score == total_score:
                if index == 0:
                    return "Gold"
                elif index == 1:
                    return "Silver"
                elif index == 2:
                    return "Bronze"

    return "No Medal"


def ski_jump_medal_proper(distance_points: float, style_points: float, wind_comp: float, k_point_bonus: float) -> str:
    total_score: float = sum([distance_points, style_points, wind_comp, k_point_bonus])
    scores: list[float] = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0, total_score]

    scores.sort(reverse=True)
    rank: int = scores.index(total_score)

    if rank == 0:
        return "Gold"
    elif rank == 1:
        return "Silver"
    elif rank == 2:
        return "Bronze"
    else:
        return "No Medal"


print(ski_jump_medal(125.0, 58.0, 0.0, 6.0))
print(ski_jump_medal(119.0, 50.0, 1.0, 4.0))
print(ski_jump_medal(122.0, 52.0, -1.0, 4.0))
print(ski_jump_medal(118.0, 50.5, -1.5, 4.0))
print(ski_jump_medal(124.0, 50.5, 2.0, 5.0))
print(ski_jump_medal(119.0, 49.5, 0.0, 3.0))
