/*
Phone Number Formatter
Given a string of eleven digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".

1. format_number("05552340182") should return "+0 (555) 234-0182".
2. format_number("15554354792") should return "+1 (555) 435-4792".
 */

function formatNumber(number) {
    const element0 = `+${number[0]}`;
    const element1 = `(${number.slice(1, 4)})`;
    const element2 = `${number.slice(4, 7)}-${number.slice(7)}`;

    return `${element0} ${element1} ${element2}`;
}


console.log(formatNumber("05552340182"));
console.log(formatNumber("15554354792"));
