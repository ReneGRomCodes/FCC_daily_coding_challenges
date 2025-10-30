"""
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers
are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.

1. nth_prime(5) should return 11.
2. nth_prime(10) should return 29.
3. nth_prime(16) should return 53.
4. nth_prime(99) should return 523.
5. nth_prime(1000) should return 7919.
"""

def nth_prime(n: int) -> int:
    """
    Find the n-th prime using the 'Sieve of Eratosthenes' method. No, I didn't come up with it myself... had to google
    this one ;)
    """
    if n == 1:
        return 2

    limit = max(15, n * 2)
    primes = []

    while len(primes) < n:
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        p = 2
        while p * p <= limit:
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
            p += 1

        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        limit *= 2

    return primes[n - 1]


print(nth_prime(5))
print(nth_prime(10))
print(nth_prime(16))
print(nth_prime(99))
print(nth_prime(1000))
