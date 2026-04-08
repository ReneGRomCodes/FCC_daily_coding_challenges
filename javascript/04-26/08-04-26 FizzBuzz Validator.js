/*
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

- Multiples of 3 are replaced with "Fizz".
- Multiples of 5 are replaced with "Buzz".
- Multiples of both 3 and 5 are replaced with "FizzBuzz".
- All other numbers remain as integers.

1. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]) should return True.
2. is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]) should return True.
3. is_fizz_buzz([1, 2, "Fizz", 4, 5]) should return False.
4. is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]) should return True.
5. is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]) should return False.
6. is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]) should return False.
7. is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]) should return True.
 */

function getOriginalSequence(arr) {
    // Find the first integer to determine the start.
    const firstIntIndex = arr.findIndex(v => typeof v === "number");
    const start = arr[firstIntIndex] - firstIntIndex;

    // Generate the full sequence.
    return Array.from({ length: arr.length }, (_, i) => start + i);
}

function isFizzBuzz(arr) {
    const originalSequence = getOriginalSequence(arr);

    // Check each element.
    return originalSequence.every((num, i) => {
        const val = arr[i];
        let correctVal;

        if (num % 15 === 0) correctVal = "FizzBuzz";
        else if (num % 3 === 0) correctVal = "Fizz";
        else if (num % 5 === 0) correctVal = "Buzz";
        else correctVal = num;

        return val === correctVal;
    });
}


console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz"]));
console.log(isFizzBuzz([13, 14, "FizzBuzz", 16, 17]));
console.log(isFizzBuzz([1, 2, "Fizz", 4, 5]));
console.log(isFizzBuzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]));
console.log(isFizzBuzz([1, 2, "Fizz", "Buzz", 5]));
console.log(isFizzBuzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]));
console.log(isFizzBuzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]));
