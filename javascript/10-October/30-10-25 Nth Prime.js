/*
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers
are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.

1. nth_prime(5) should return 11.
2. nth_prime(10) should return 29.
3. nth_prime(16) should return 53.
4. nth_prime(99) should return 523.
5. nth_prime(1000) should return 7919.
 */

function nthPrime(n) {
    if (n === 1) { return 2 }

    let limit = Math.max(15, n * 2);
    let primes = [];

    while (primes.length < n) {
        const sieve = new Array(limit + 1).fill(true);
        sieve[0] = false;
        sieve[1] = false;

        let p = 2;

        while (p * p <= limit) {
            if (sieve[p]) {
                for (let i = p * p; i <= limit; i += p) {
                    sieve[i] = false;
                }
            }
            p++;
        }

        primes = [];

        for (let i = 0; i < sieve.length; i++) {
            if (sieve[i]) {
                primes.push(i);
            }
        }

        limit *= 2;
    }

    return primes[n - 1];
}


console.log(nthPrime(5));
console.log(nthPrime(10));
console.log(nthPrime(16));
console.log(nthPrime(99));
console.log(nthPrime(1000));
