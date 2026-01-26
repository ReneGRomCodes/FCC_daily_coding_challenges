/*
FizzBuzz Mini
Given an integer, return a string based on the following rules:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 5, return "Buzz".
If the number is divisible by both 3 and 5, return "FizzBuzz".
Otherwise, return the given number as a string.

1. fizz_buzz_mini(3) should return "Fizz".
2. fizz_buzz_mini(4) should return "4".
3. fizzBuzzMini(35) should return "Buzz".
4. fizzBuzzMini(75) should return "FizzBuzz".
5. fizzBuzzMini(98) should return "98".
 */

function fizzBuzzMini(n) {
    if (n % 3 === 0 && n % 5 === 0) {
        return "FizzBuzz";
    } else if (n % 3 === 0) {
        return "Fizz";
    } else if (n % 5 === 0) {
        return "Buzz";
    }

    return n.toString();
}


console.log(fizzBuzzMini(3));
console.log(fizzBuzzMini(4));
console.log(fizzBuzzMini(35));
console.log(fizzBuzzMini(75));
console.log(fizzBuzzMini(98));
