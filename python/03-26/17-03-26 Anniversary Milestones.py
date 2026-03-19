"""
Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary
milestone according to this chart:

Years Married	Milestone
1	            "Paper"
5	            "Wood"
10	            "Tin"
25	            "Silver"
40	            "Ruby"
50	            "Gold"
60	            "Diamond"
70	            "Platinum"

If they haven't reached the first milestone, return "Newlyweds".

1. get_milestone(0) should return "Newlyweds".
2. get_milestone(1) should return "Paper".
3. get_milestone(8) should return "Wood".
4. get_milestone(10) should return "Tin".
5. get_milestone(26) should return "Silver".
6. get_milestone(45) should return "Ruby".
7. get_milestone(50) should return "Gold".
8. get_milestone(64) should return "Diamond".
9. get_milestone(71) should return "Platinum".
"""

def get_milestone(years: int) -> str:
    if years >= 70:
        return "Platinum"
    elif years >= 60:
        return "Diamond"
    elif years >= 50:
        return "Gold"
    elif years >= 40:
        return "Ruby"
    elif years >= 25:
        return "Silver"
    elif years >= 10:
        return "Tin"
    elif years >= 5:
        return "Wood"
    elif years >= 1:
        return "Paper"
    else:
        return "Newlyweds"


print(get_milestone(0))
print(get_milestone(1))
print(get_milestone(8))
print(get_milestone(10))
print(get_milestone(26))
print(get_milestone(45))
print(get_milestone(50))
print(get_milestone(64))
print(get_milestone(71))
