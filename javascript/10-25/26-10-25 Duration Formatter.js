/*
Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H"
is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the
following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.

1. format(500) should return "8:20".
2. format(4000) should return "1:06:40".
3. format(1) should return "0:01".
4. format(5555) should return "1:32:35".
5. format(99999) should return "27:46:39".
 */

function format(seconds) {

    return seconds;
}


console.log(format(500));
console.log(format(4000));
console.log(format(1));
console.log(format(5555));
console.log(format(99999));
