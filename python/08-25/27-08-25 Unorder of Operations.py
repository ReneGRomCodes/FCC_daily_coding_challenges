"""
Unorder of Operations
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from
left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right
ignoring standard order of operations.

Valid operators are +, -, *, /, and %.

1. evaluate([5, 6, 7, 8, 9], ['+', '-']) should return 3
2. evaluate([17, 61, 40, 24, 38, 14], ['+', '%']) should return 38
3. evaluate([20, 2, 4, 24, 12, 3], ['*', '/']) should return 60
4. evaluate([11, 4, 10, 17, 2], ['*', '*', '%']) should return 30
5. evaluate([33, 11, 29, 13], ['/', '-']) should return -2
"""

def apply_op(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return int(a / b)
    elif op == '%': return a % b
    return None


def evaluate(numbers: list[int], operators: list[str]) -> int:
    op_index: int = 0
    op_indices: list[int] = []
    evaluation = numbers[0]

    # Populate list with operator list indices that corresponds to 'numbers' list.
    for _ in numbers:
        op_indices.append(op_index)

        if op_index == len(operators) - 1:
            op_index = 0
        else:
            op_index +=1

    for index, (num, op_index) in enumerate(zip(numbers, op_indices)):
        if index == len(numbers) - 1:  # Return final result when last index is reached.
            return evaluation
        else:
            evaluation = apply_op(evaluation, numbers[index + 1], operators[op_index])

    return evaluation


print(evaluate([5, 6, 7, 8, 9], ['+', '-']))
print(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']))
print(evaluate([20, 2, 4, 24, 12, 3], ['*', '/']))
print(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']))
print(evaluate([33, 11, 29, 13], ['/', '-']))
