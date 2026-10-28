/*
Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).

1. is_spam("+0 (200) 234-0182") should return False.
2. is_spam("+091 (555) 309-1922") should return True.
3. is_spam("+1 (555) 435-4792") should return True.
4. is_spam("+0 (955) 234-4364") should return True.
5. is_spam("+0 (155) 131-6943") should return True.
6. is_spam("+0 (555) 135-0192") should return True.
7. is_spam("+0 (555) 564-1987") should return True.
8. is_spam("+00 (555) 234-0182") should return False.
 */

function isSpam(number) {
    const elements = number.split(" ");

    const countryCode = elements[0].replace("+", "");
    const areaCode = elements[1].replace("(", "").replace(")", "");
    const localNumber = elements[2].split("-");
    const fullNumberString = countryCode + areaCode + localNumber[0] + localNumber[1];

    if (countryCode.length > 2 || countryCode[0] !== "0") {
        return true;
    } else if (!(200 <= Number(areaCode) && Number(areaCode) <= 900)) {
        return true;
    } else if (localNumber[1].includes(String([...localNumber[0]].reduce((sum, x) => sum + Number(x), 0)))) {
        return true;
    }

    for (let i = 0; i < 10; i++) {
        if (fullNumberString.includes(i.toString().repeat(4))) {
            return true;
        }
    }

    return false;
}


console.log(isSpam("+0 (200) 234-0182"));
console.log(isSpam("+091 (555) 309-1922"));
console.log(isSpam("+1 (555) 435-4792"));
console.log(isSpam("+0 (955) 234-4364"));
console.log(isSpam("+0 (155) 131-6943"));
console.log(isSpam("+0 (555) 135-0192"));
console.log(isSpam("+0 (555) 564-1987"));
console.log(isSpam("+00 (555) 234-0182"));
