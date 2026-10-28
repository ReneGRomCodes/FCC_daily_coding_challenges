/*
Prime Factorization
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.

A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has
exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.

If the given integer is itself prime, return it in a single-element array.

1. prime_factorization(20) should return [2, 2, 5].
2. prime_factorization(17) should return [17].
3. prime_factorization(15) should return [3, 5].
4. prime_factorization(35) should return [5, 7].
5. prime_factorization(999) should return [3, 3, 3, 37].
6. prime_factorization(360) should return [2, 2, 2, 3, 3, 5].
7. prime_factorization(510510) should return [2, 3, 5, 7, 11, 13, 17].
 */

function primeFactorization(n) {
    const factors = [];
    let divisor = 2;

    while (n > 1) {
        if (n % divisor === 0) {
            factors.push(divisor);
            n = Math.floor(n / divisor);
        } else {
            divisor += 1;
        }
    }

    return factors;
}


console.log(primeFactorization(20));
console.log(primeFactorization(17));
console.log(primeFactorization(15));
console.log(primeFactorization(35));
console.log(primeFactorization(999));
console.log(primeFactorization(360));
console.log(primeFactorization(510510));
