/*
Equation Validation
Given a string representing a math equation, determine whether it is correct.

- The left side may contain up to three positive integers and the operators +, -, *, and /.
- The equation will be given in the format: "number operator number = number" (with two or three numbers on the left).
  For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
- The right side will always be a single integer.

Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from
left-to-right.

1. is_valid_equation("2 + 2 = 4") should return True.
2. is_valid_equation("2 + 3 - 1 = 4") should return True.
3. is_valid_equation("8 / 2 = 4") should return True.
4. is_valid_equation("10 * 5 = 50") should return True.
5. is_valid_equation("2 - 2 = 0") should return True.
6. is_valid_equation("2 + 9 / 3 = 5") should return True.
7. is_valid_equation("20 - 2 * 3 = 14") should return True.
8. is_valid_equation("2 + 5 = 6") should return False.
9. is_valid_equation("10 - 2 * 3 = 24") should return False.
10. is_valid_equation("3 + 9 / 3 = 4") should return False.
 */

function isValidEquation(equation) {
    // DON'T ever do it like this in the real world! 'eval' does the trick here but is risky as hell. Why did I use it
    // then? It's Sunday morning and just couldn't be bothered to find a proper solution... don't look at me like that!
    // We all have these days ;)
    const [left, right] = equation.split("=");

    return eval(left.trim()) === Number(right.trim());
}

console.log(isValidEquation("2 + 2 = 4"));
console.log(isValidEquation("2 + 3 - 1 = 4"));
console.log(isValidEquation("8 / 2 = 4"));
console.log(isValidEquation("10 * 5 = 50"));
console.log(isValidEquation("2 - 2 = 0"));
console.log(isValidEquation("2 + 9 / 3 = 5"));
console.log(isValidEquation("20 - 2 * 3 = 14"));
console.log(isValidEquation("2 + 5 = 6"));
console.log(isValidEquation("10 - 2 * 3 = 24"));
console.log(isValidEquation("3 + 9 / 3 = 4"));
