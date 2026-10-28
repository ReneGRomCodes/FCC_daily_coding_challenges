/*
Evenly Divisible

Given two integers, determine if you can evenly divide the first one by the second one.

1. is_evenly_divisible(4, 2) should return True.
2. is_evenly_divisible(7, 3) should return False.
3. is_evenly_divisible(5, 10) should return False.
4. is_evenly_divisible(48, 6) should return True.
5. is_evenly_divisible(3186, 9) should return True.
6. is_evenly_divisible(4192, 11) should return False.
 */

function isEvenlyDivisible(a, b) {
    return a % b === 0;
}


console.log(isEvenlyDivisible(4, 2));
console.log(isEvenlyDivisible(7, 3));
console.log(isEvenlyDivisible(5, 10));
console.log(isEvenlyDivisible(48, 6));
console.log(isEvenlyDivisible(3186, 9));
console.log(isEvenlyDivisible(4192, 11));
