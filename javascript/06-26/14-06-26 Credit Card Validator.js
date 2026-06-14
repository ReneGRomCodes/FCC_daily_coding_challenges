/*
Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:

- Starting from the second-to-last digit, double every other digit moving left.
- If doubling a digit results in a number greater than 9, subtract 9.
- Sum all the digits (doubled and undoubled).
- If the total is divisible by 10, the number is valid.

1. is_valid_card("4532015112830366") should return True.
2. is_valid_card("5425233430109903") should return True.
3. is_valid_card("371449635398431") should return True.
4. is_valid_card("6011111111111117") should return True.
5. is_valid_card("4532015112830367") should return False.
6. is_valid_card("1234567890123456") should return False.
7. is_valid_card("4532015112830368") should return False.
 */

function isValidCard(number) {
    const reversedN = [...number].reverse().map(Number);
    let totalSum = 0;

    for (let i = 0; i < reversedN.length; i++) {
        if (i % 2 !== 0) {
            let m = reversedN[i] * 2;
            m <= 9 ? totalSum += m : totalSum += m - 9;
        } else {
            totalSum += reversedN[i];
        }
    }

    return totalSum % 10 === 0;
}


console.log(isValidCard("4532015112830366"));
console.log(isValidCard("5425233430109903"));
console.log(isValidCard("371449635398431"));
console.log(isValidCard("6011111111111117"));
console.log(isValidCard("4532015112830367"));
console.log(isValidCard("1234567890123456"));
console.log(isValidCard("4532015112830368"));
