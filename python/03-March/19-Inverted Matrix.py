"""
Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one
value are swapped with the other.

For example, given:
[
  ["a", "b"],
  ["a", "a"]
]

Return:
[
  ["b", "a"],
  ["b", "b"]
]

1. invert_matrix([["a", "b"], ["a", "a"]]) should return [["b", "a"], ["b", "b"]].
2. invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) should return [[0, 1, 0], [0, 0, 0], [1, 0, 1]].
3. invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])
    should return [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]].
4. invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])
    should return [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]].
5. invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])
    should return [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]].
"""

def invert_matrix(matrix: list[list]) -> list[list]:
    values: tuple = ()
    inverted_matrix: list[list] = []

    # Get unique values.
    for item in matrix:
        values = tuple(set(item))
        # Ensure both unique values have been found.
        if len(values) == 2:
            break

    # Build inverted matrix.
    for item in matrix:
        inverted_item: list = []

        for value in item:
            if value == values[0]:
                inverted_item.append(values[1])
            else:
                inverted_item.append(values[0])

        inverted_matrix.append(inverted_item)

    return inverted_matrix


print(invert_matrix([["a", "b"], ["a", "a"]]))
print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))
print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]))
print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]))
print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]))
