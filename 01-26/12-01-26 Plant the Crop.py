"""
Plant the Crop
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size
of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

1 acre equals 4046.86 square meters.
1 hectare equals 10,000 square meters.
Here's a list of crops that will be given as input and how much space a single plant takes:

Crop	Space per plant
"corn"	1 square meter
"wheat"	0.1 square meters
"soybeans"	0.5 square meters
"tomatoes"	0.25 square meters
"lettuce"	0.2 square meters
Return the number of plants that fit in the field, rounded down to the nearest whole plant.

1. get_number_of_plants(1, "acres", "corn") should return 4046.
2. get_number_of_plants(2, "hectares", "lettuce") should return 100000.
3. get_number_of_plants(20, "acres", "soybeans") should return 161874.
4. get_number_of_plants(3.75, "hectares", "tomatoes") should return 150000.
5. get_number_of_plants(16.75, "acres", "tomatoes") should return 271139.
"""

SQRM_CONVERSION: dict[str, float] = {
    "acres": 4046.86,
    "hectares": 10000.0,
}

CROPS_SQRM: dict[str, float] = {
    "corn": 1.0,
    "wheat": 0.1,
    "soybeans": 0.5,
    "tomatoes": 0.25,
    "lettuce": 0.2,
}

def get_number_of_plants(field_size: int | float, unit: str, crop: str) -> int:
    return int(field_size * SQRM_CONVERSION[unit] / CROPS_SQRM[crop])


print(get_number_of_plants(1, "acres", "corn"))
print(get_number_of_plants(2, "hectares", "lettuce"))
print(get_number_of_plants(20, "acres", "soybeans"))
print(get_number_of_plants(3.75, "hectares", "tomatoes"))
print(get_number_of_plants(16.75, "acres", "tomatoes"))
