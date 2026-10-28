/*
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
 */

function applyOp(a, b, op) {
    if (op === "+") return a + b;
    else if (op === "-") return a - b;
    else if (op === "*") return a * b;
    else if (op === "/") return a / b;
    else if (op === "%") return a % b;
}


function evaluate(numbers, operators) {
    let opIndex = 0;
    const opIndices = [];
    let evaluation = numbers[0];

    for (const _ of numbers) {
        opIndices.push(opIndex);
        opIndex === operators.length - 1 ? opIndex = 0 : opIndex++;
    }

    for (let index = 0; index < numbers.length; index++) {
        if (index === numbers.length - 1) {
            return evaluation;
        }

        evaluation = applyOp(
            evaluation,
            numbers[index + 1],
            operators[opIndices[index]]
        );
    }

    return evaluation;
}


console.log(evaluate([5, 6, 7, 8, 9], ['+', '-']));
console.log(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']));
console.log(evaluate([20, 2, 4, 24, 12, 3], ['*', '/']));
console.log(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']));
console.log(evaluate([33, 11, 29, 13], ['/', '-']));
