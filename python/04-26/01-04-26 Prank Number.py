"""
Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't
follow the pattern fixed.

The pattern will be one of:
- The numbers increase from one to the next by a fixed amount (addition).
- The numbers decrease from one to the next by a fixed amount (subtraction).

For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

1. fix_prank_number([2, 4, 7, 8, 10]) should return [2, 4, 6, 8, 10].
2. fix_prank_number([10, 10, 8, 7, 6]) should return [10, 9, 8, 7, 6].
3. fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]) should return [12, 24, 36, 48, 60, 72, 84, 96].
4. fix_prank_number([4, 1, -2, -5, -8, -5]) should return [4, 1, -2, -5, -8, -11].
5. fix_prank_number([0, 100, 200, 300, 150, 500]) should return [0, 100, 200, 300, 400, 500].
6. fix_prank_number([400, 425, 400, 375, 350, 325, 300]) should return [450, 425, 400, 375, 350, 325, 300].
7. fix_prank_number([-5, 5, 10, 15, 20]) should return [0, 5, 10, 15, 20].
"""

def fix_prank_number(arr: list[int]) -> list[int]:
    # Find correct steps.
    steps: list[int] = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    correct_step: int = max(set(steps), key=steps.count)

    # Helper function to build a candidate sequence.
    def build_candidate(start: int) -> list[int]:
        return [start + i * correct_step for i in range(len(arr))]

    # Build candidate sequence for fixed array assuming first element is correct.
    candidate_sequence: list[int] = build_candidate(arr[0])

    # Count mismatches between 'candidate_sequence' and 'arr'.
    mismatches: int = sum(1 for a, b in zip(arr, candidate_sequence) if a != b)

    if mismatches <= 1:
        return candidate_sequence
    else:
        # First element must be wrong -> recompute sequence from second element.
        start: int = arr[1] - correct_step
        return build_candidate(start)


print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([0, 100, 200, 300, 150, 500]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))
