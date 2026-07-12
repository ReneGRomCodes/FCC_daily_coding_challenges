/*
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number

If the final value is zero (0), return 13.

1. get_lucky_number("John Doe") should return 21.
2. get_lucky_number("Olivia Lewis") should return 52.
3. get_lucky_number("James Wilson") should return 18.
4. get_lucky_number("Elizabeth Hernandez") should return 81.
5. get_lucky_number("Mike Walker") should return 32.
6. get_lucky_number("Chloe Perez") should return 13.
 */

function getVowelConsonantCount(str) {
    const vowels = "aeiou";
    let [vowelCount, consonantCount] = [0, 0];

    for (const char of str.toLowerCase()) { vowels.includes(char) ? vowelCount += 1 : consonantCount += 1; }

    return [vowelCount, consonantCount];
}


function getLuckyNumber(name) {
    const [firstName, lastName] = name.split(" ");
    const [fnVowelCount, fnConsonantCount] = getVowelConsonantCount(firstName);
    const [lnVowelCount, lnConsonantCount] = getVowelConsonantCount(lastName);

    // Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name.
    const smallerVal = (Math.min(fnVowelCount, lnVowelCount) * Math.min(fnConsonantCount, lnConsonantCount) *
        Math.min(firstName.length, lastName.length));

    // Do the same for the two larger counts and the larger name.
    const largerVal = (Math.max(fnVowelCount, lnVowelCount) * Math.max(fnConsonantCount, lnConsonantCount) *
        Math.max(firstName.length, lastName.length));

    const luckyNumber = largerVal - smallerVal;

    return luckyNumber === 0 ? 13 : luckyNumber;
}


console.log(getLuckyNumber("John Doe"));
console.log(getLuckyNumber("Olivia Lewis"));
console.log(getLuckyNumber("James Wilson"));
console.log(getLuckyNumber("Elizabeth Hernandez"));
console.log(getLuckyNumber("Mike Walker"));
console.log(getLuckyNumber("Chloe Perez"));
