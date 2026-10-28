/*
Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

Kaprekar's routine works as follows:

- Arrange the digits in descending order to form the largest number
- Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
- Subtract the smaller from the larger
- Repeat with the new number

1. kaprekar(1234) should return 3.
2. kaprekar(2025) should return 6.
3. kaprekar(7173) should return 4.
4. kaprekar(3164) should return 7.
5. kaprekar(8082) should return 2.
 */

function getNumbers(n) {
    const digits = String(n).padStart(4, "0").split("");

    const ascending = [...digits].sort();
    const descending = [...ascending].reverse();

    return [
        Number(descending.join("")),
        Number(ascending.join(""))
    ];
}

function kaprekar(n) {
    let count = 0;

    while (n !== 6174) {
        const [larger, smaller] = getNumbers(n);
        n = larger - smaller;

        if (n === 0) break; // Avoid infinite loop. Useless for the given test cases, but I feel funky today ;)

        count++;
    }

    return count;
}


console.log(kaprekar(1234));
console.log(kaprekar(2025));
console.log(kaprekar(7173));
console.log(kaprekar(3164));
console.log(kaprekar(8082));
