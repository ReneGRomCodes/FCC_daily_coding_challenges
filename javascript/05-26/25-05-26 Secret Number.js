/*
Secret Number
Given a secret number and a guess, determine if the guess is correct.

Return:
- "higher" if the secret number is higher than the guess.
- "lower" if the secret number is lower than the guess.
- "you got it!" if the guess is correct.

1. guess_number(50, 30) should return "higher".
2. guess_number(85, 99) should return "lower".
3. guess_number(2026, 2026) should return "you got it!".
4. guess_number(92904, 11283) should return "higher".
5. guess_number(230495, 423920) should return "lower".
6. guess_number(120349, 120349) should return "you got it!".
 */

function guessNumber(secret, guess) {
    return guess < secret ? "higher" : guess > secret ? "lower" : "you got it!";
}


console.log(guessNumber(50, 30));
console.log(guessNumber(85, 99));
console.log(guessNumber(2026, 2026));
console.log(guessNumber(92904, 11283));
console.log(guessNumber(230495, 423920));
console.log(guessNumber(120349, 120349));
