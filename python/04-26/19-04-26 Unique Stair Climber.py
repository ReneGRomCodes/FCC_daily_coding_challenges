"""
Unique Stair Climber
Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.

1. get_unique_climbs(4) should return 5.
2. get_unique_climbs(5) should return 8.
3. get_unique_climbs(10) should return 89.
4. get_unique_climbs(18) should return 4181.
5. get_unique_climbs(29) should return 832040.
6. get_unique_climbs(50) should return 20365011074.
"""

def get_unique_climbs(steps: int) -> int:
    if steps <= 2:
        return steps

    n, m = 1, 2
    for _ in range(3, steps + 1):
        n, m = m, n + m

    return m


print(get_unique_climbs(4))
print(get_unique_climbs(5))
print(get_unique_climbs(10))
print(get_unique_climbs(18))
print(get_unique_climbs(29))
print(get_unique_climbs(50))
