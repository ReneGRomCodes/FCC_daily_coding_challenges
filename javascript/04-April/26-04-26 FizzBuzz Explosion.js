/*
FizzBuzz Explosion

Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given
number of "z"'s using the following rules:
- Start with the string "fizzbuzz".
- Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
    - If the letter position is divisible by 3, replace the letter with "fizz"
    - If it's divisible by 5, replace the letter with "buzz"
    - If it's divisible by 3 and 5, replace the letter with "fizzbuzz"

So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.

1. explodeFizzbuzz(9) should return 1.
2. explodeFizzbuzz(15) should return 2.
3. explodeFizzbuzz(51) should return 3.
4. explodeFizzbuzz(52) should return 4.
5. explodeFizzbuzz(359) should return 5.
6. explodeFizzbuzz(789) should return 6.
7. explodeFizzbuzz(54482) should return 11.
8. explodeFizzbuzz(1000000) should return 14.
 */

function explodeFizzbuzz(targetZCount) {
    let startFizzbuzz = "fizzbuzz";
    let explodedFizzbuzz = [];
    let steps = 0;

    while (true) {
        for (let pos = 1; pos <= startFizzbuzz.length; pos++) {
            const isFizz = pos % 3 === 0;
            const isBuzz = pos % 5 === 0;
            const isFizzbuzz = isFizz && isBuzz;

            if (isFizzbuzz) {
                explodedFizzbuzz.push("fizzbuzz");
            } else if (isFizz) {
                explodedFizzbuzz.push("fizz");
            } else if (isBuzz) {
                explodedFizzbuzz.push("buzz");
            } else {
                explodedFizzbuzz.push(startFizzbuzz[pos - 1]);
            }
        }

        steps++;
        const explodedFizzbuzzStr = explodedFizzbuzz.join("");

        if ([...explodedFizzbuzzStr].filter(char => char === "z").length >= targetZCount) {
            return steps
        }

        startFizzbuzz = explodedFizzbuzzStr;
        explodedFizzbuzz = [];
    }
}


console.log(explodeFizzbuzz(9));
console.log(explodeFizzbuzz(15));
console.log(explodeFizzbuzz(51));
console.log(explodeFizzbuzz(52));
console.log(explodeFizzbuzz(359));
console.log(explodeFizzbuzz(789));
console.log(explodeFizzbuzz(54482));
console.log(explodeFizzbuzz(1000000));
