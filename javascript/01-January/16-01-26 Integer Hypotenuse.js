/*
Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle,
determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the
square root of that total (a² + b² = c²).

1. is_integer_hypotenuse(3, 4) should return True.
2. is_integer_hypotenuse(2, 3) should return False.
3. is_integer_hypotenuse(5, 12) should return True.
4. is_integer_hypotenuse(10, 10) should return False.
5. is_integer_hypotenuse(780, 1040) should return True.
6. is_integer_hypotenuse(250, 333) should return False.
 */

function isIntegerHypotenuse(a, b) { return Math.sqrt(a**2 + b**2) % 1 === 0 }


console.log(isIntegerHypotenuse(3, 4));
console.log(isIntegerHypotenuse(2, 3));
console.log(isIntegerHypotenuse(5, 12));
console.log(isIntegerHypotenuse(10, 10));
console.log(isIntegerHypotenuse(780, 1040));
console.log(isIntegerHypotenuse(250, 333));
