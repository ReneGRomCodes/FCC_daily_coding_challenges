"""
BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.

To get BMI: divide the weight by the height squared, then multiply the result by 703.

1. calculate_bmi(180, 70) should return 25.8.
2. calculate_bmi(140, 64) should return 24.0.
3. calculate_bmi(160, 76) should return 19.5.
4. calculate_bmi(200, 60) should return 39.1.
5. calculate_bmi(150, 68) should return 22.8.
"""

def calculate_bmi(weight: int, height: int) -> float:
    return round((weight / height**2) * 703, 1)


print(calculate_bmi(180, 70))
print(calculate_bmi(140, 64))
print(calculate_bmi(160, 76))
print(calculate_bmi(200, 60))
print(calculate_bmi(150, 68))
