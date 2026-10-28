"""
2026 Winter Games Day 12: Bobsled
Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the
bobsled, determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by iteself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team

The total weight of the bobsled (athletes plus sled) must not exceed:

247 kg for a 1-person team
390 kg for a 2-person team
630 kg for a 4-person team

Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the
requirements.

1. check_eligibility([78], 165) should return "Eligible".
2. check_eligibility([80], 160) should return "Not Eligible".
3. check_eligibility([80], 170) should return "Not Eligible".
4. check_eligibility([85, 90], 170) should return "Eligible".
5. check_eligibility([85, 95], 168) should return "Not Eligible".
6. check_eligibility([112, 97], 185) should return "Not Eligible".
7. check_eligibility([110, 102, 90, 106], 222) should return "Eligible".
8. check_eligibility([106, 99, 90, 88], 205) should return "Not Eligible".
9. check_eligibility([106, 99, 103, 96], 227) should return "Not Eligible".
"""

def check_eligibility(athlete_weights: list[int], sled_weight: int) -> str:
    weight_limits: dict[int, dict[str, int]] = {
        1: {"sled_min": 162,
            "total_max": 247,},
        2: {"sled_min": 170,
            "total_max": 390,},
        4: {"sled_min": 210,
            "total_max": 630,},
    }
    team_size: int = len(athlete_weights)
    total_weight: int = sum(athlete_weights) + sled_weight

    if total_weight > weight_limits[team_size]["total_max"] or sled_weight < weight_limits[team_size]["sled_min"]:
        return "Not Eligible"
    else:
        return "Eligible"


print(check_eligibility([78], 165))
print(check_eligibility([80], 160))
print(check_eligibility([80], 170))
print(check_eligibility([85, 90], 170))
print(check_eligibility([85, 95], 168))
print(check_eligibility([112, 97], 185))
print(check_eligibility([110, 102, 90, 106], 222))
print(check_eligibility([106, 99, 90, 88], 205))
print(check_eligibility([106, 99, 103, 96], 227))
