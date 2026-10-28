/*
Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.

1. is_circular_prime(197) should return True.
2. is_circular_prime(23) should return False.
3. is_circular_prime(13) should return True.
4. is_circular_prime(89) should return False.
5. is_circular_prime(1193) should return True.
 */

function isPrime(x) {
    if (x < 2 || x % 2 === 0) { return false }
    if (x === 2) { return true }

    let i = 3;
    while (i * i <= x) {
        if (x % i === 0) { return false }
        i += 2;
    }

    return true;
}


function isCircularPrime(n) {
    const s = String(n);
    const length = s.length;

    for (let i = 0; i < length; i++) {
        const rotation = Number(s.slice(i) + s.slice(0, i));

        if (!isPrime(rotation)) {
            return false;
        }
    }

    return true;
}


console.log(isCircularPrime(197));
console.log(isCircularPrime(23));
console.log(isCircularPrime(13));
console.log(isCircularPrime(89));
console.log(isCircularPrime(1193));
