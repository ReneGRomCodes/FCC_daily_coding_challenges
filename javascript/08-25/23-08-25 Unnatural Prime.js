/*
Unnatural Prime
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.

1. is_unnatural_prime(1) should return False.
2. is_unnatural_prime(-1) should return False.
3. is_unnatural_prime(19) should return True.
4. is_unnatural_prime(-23) should return True.
5. is_unnatural_prime(0) should return False.
6. is_unnatural_prime(97) should return True.
7. is_unnatural_prime(-61) should return True.
8. is_unnatural_prime(99) should return False.
9. is_unnatural_prime(-44) should return False.
 */

function isUnnaturalPrime(n) {
    const absN = Math.abs(n);

    if (absN < 2) {
        return false;
    }

    for (let i=2; i <= Math.floor(absN / 2); i++) {
        if (absN % i === 0) {
            return false;
        }
    }

    return true;
}


console.log(isUnnaturalPrime(1));
console.log(isUnnaturalPrime(-1));
console.log(isUnnaturalPrime(19));
console.log(isUnnaturalPrime(-23));
console.log(isUnnaturalPrime(0));
console.log(isUnnaturalPrime(97));
console.log(isUnnaturalPrime(-61));
console.log(isUnnaturalPrime(99));
console.log(isUnnaturalPrime(-44));
