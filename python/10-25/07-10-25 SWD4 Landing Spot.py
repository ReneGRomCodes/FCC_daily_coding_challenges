"""
Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots
for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest
total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]

Return [0, 1], the indices for the 0 in the first array.

1. find_landing_spot([[1, 0], [2, 0]]) should return [0, 1].
2. find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) should return [1, 1].
3. find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) should return [2, 2].
4. find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) should return [2, 1].
"""

def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    landing_spots_dict: dict[tuple[int, int], int] = {}

    for arr_index, array in enumerate(matrix):
        for spt_index, spot in enumerate(array):
            if spot == 0:
                # Dict of the spots coord (indices) as keys and 'danger rating' (sum of the surrounding fields) as values.
                landing_spots_dict[arr_index, spt_index] = 0

                # Check 'east' and 'west' if possible.
                if spt_index != 0:
                    landing_spots_dict[arr_index, spt_index] += array[spt_index-1]
                if spt_index != (len(array) - 1):
                    landing_spots_dict[arr_index, spt_index] += array[spt_index+1]
                # Check 'north' and 'south' if possible.
                if arr_index != 0:
                    landing_spots_dict[arr_index, spt_index] += matrix[arr_index - 1][spt_index]
                if arr_index != (len(array) - 1):
                    landing_spots_dict[arr_index, spt_index] += matrix[arr_index + 1][spt_index]

    safest_landing_spot: list[int] = list(min(landing_spots_dict, key=landing_spots_dict.get))

    return safest_landing_spot


print(find_landing_spot([[1, 0], [2, 0]]))
print(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]))
print(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]))
print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))
