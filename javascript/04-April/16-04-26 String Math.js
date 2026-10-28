/*
String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters
between the numbers.

- If the count of characters separating two numbers is even, use addition.
- If it's odd, use subtraction.
- Consecutive digits form a single number.
- Operations are applied left to right.
- Ignore leading and trailing characters that aren't digits.

For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them.
Then subtract 8 from 13 because there's an odd number of characters between the result and 8.

1. do_math("3ab10c8") should return 5.
2. do_math("6MINUS4") should return 2.
3. do_math("9plus3") should return 12.
4. do_math("5fkwo#10i#%.<>15P=@20!#B/25") should return 15.
5. do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt") should return 67.
 */

function splitStoNumeric(str) {
    const sSplit = [];
    let section = "";

    for (let i = 0; i < str.length; i++) {
        // Find first numeric character and add to 'section'.
        const char = str[i];
        const isNumeric = char >= "0" && char <= "9";

        if (!section) {
            if (isNumeric) {
                section += char;
            } else {
                continue;
            }
        /*
        Split numeric from non-numeric characters by checking if current char is of same type as previous char in
        'section'. Add 'section' to 's_split' if not and start new 'section' variable.
         */
        } else {
            const isPreviousNumeric = section[section.length - 1] >= "0" && section[section.length - 1] <= "9";

            if (isNumeric !== isPreviousNumeric) {
                sSplit.push(section);
                section = char;
            } else {
                section += char;
            }
        }

        // Ensure last section is only added if it is numeric.
        if (i === str.length - 1 && isNumeric) {
            sSplit.push(section);
        }
    }

    return sSplit;
}


function doMath(str) {
    const sSplit = splitStoNumeric(str);
    let sumN = Number(sSplit[0]);

    for (let i = 0; i < sSplit.length; i++) {
        // Odd indices (except [0]) indicate operator sections.
        const isOperator = i % 2 !== 0 && i !== 0;
        const section = sSplit[i];

        if (isOperator) {
            // Addition.
            if (section.length % 2 === 0) {
                sumN += Number(sSplit[i + 1]);

            // Subtraction.
            } else {
                sumN -= Number(sSplit[i + 1]);
            }
        }
    }

    return sumN;
}


console.log(doMath("3ab10c8"));
console.log(doMath("6MINUS4"));
console.log(doMath("9plus3"));
console.log(doMath("5fkwo#10i#%.<>15P=@20!#B/25"));
console.log(doMath("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"));
