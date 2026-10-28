"""
Pet Age Calculator
Given a pet type and age in human years, return the equivalent age in pet years using the following conversion table:

Pet	            Multiplier
"dog"	        7
"cat"	        6
"rabbit"	    8
"hamster"	    30
"guinea pig"	12
"goldfish"  	6
"bird"	        5

1. pet_years("dog", 5) should return 35.
2. pet_years("cat", 9) should return 54.
3. pet_years("rabbit", 3) should return 24.
4. pet_years("hamster", 4) should return 120.
5. pet_years("guinea pig", 5) should return 60.
6. pet_years("goldfish", 2) should return 12.
7. pet_years("bird", 1) should return 5.
"""

def pet_years(pet: str, age: int) -> int:
    pet_age_multiplier: dict[str, int] = {
    "dog": 7,
    "cat": 6,
    "rabbit": 8,
    "hamster": 30,
    "guinea pig": 12,
    "goldfish": 6,
    "bird": 5,
    }

    return pet_age_multiplier[pet.lower()] * age


print(pet_years("dog", 5))
print(pet_years("cat", 9))
print(pet_years("rabbit", 3))
print(pet_years("guinea pig", 5))
print(pet_years("guinea pig", 5))
print(pet_years("goldfish", 2))
print(pet_years("bird", 1))
