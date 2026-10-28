/*
BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is
correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.

1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
2. is_fizz_buzz([1, 2, 3, 4]) should return False.
3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
4. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) should return False.
5. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) should return False.
6. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) should return False.
7. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz",
    19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37,
    38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) should return True.
 */

// Copied over this function from the solution for yesterday's challenge.
function fizzBuzz(n) {
    const fizzbuzz = [];

    for (let i = 1; i <= n; i++) {
        const fizz = i % 3 === 0;
        const buzz = i % 5 === 0;

        if (fizz && buzz) {
            fizzbuzz.push("FizzBuzz");
            continue;
        } else if (fizz) {
            fizzbuzz.push("Fizz");
            continue;
        } else if (buzz) {
            fizzbuzz.push("Buzz");
            continue;
        } else {
            fizzbuzz.push(i);
        }
    }

    return fizzbuzz;
}


function isFizzBuzz(sequence) {
    const expected = fizzBuzz(sequence.length);
    return sequence.every((value, i) => value === expected[i]);
}


console.log(isFizzBuzz([1, 2, "Fizz", 4]));
console.log(isFizzBuzz([1, 2, 3, 4]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", 7]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz",
    19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37,
    38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]));
