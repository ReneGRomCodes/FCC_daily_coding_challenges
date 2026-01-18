"""
Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your
destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.

1. fuel_to_add(0, 1) should return 1.
2. fuel_to_add(5, 40) should return 6.
3. fuel_to_add(10, 30) should return 0.
4. fuel_to_add(896, 20500) should return 4520.
5. fuel_to_add(1000, 50000) should return 12209.
"""

def fuel_to_add(current_gallons: int, required_liters: int) -> int:
    required_gallons: float = required_liters / 3.78541

    if current_gallons >= required_gallons:
        return 0

    return round(required_gallons - current_gallons + 0.5)


print(fuel_to_add(0, 1))
print(fuel_to_add(5, 40))
print(fuel_to_add(10, 30))
print(fuel_to_add(896, 20500))
print(fuel_to_add(1000, 50000))
