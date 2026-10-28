/*
Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on
your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.

1. too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) should return False.
2. too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) should return False.
3. too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) should return False.
4. too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) should return True.
5. too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) should return True.
6. too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) should return True.
7. too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) should return True.
 */

function tooMuchScreenTime(hours) {
    if (hours.reduce((a, b) => a + b, 0) / hours.length >= 6) { return true; }

    for (const day of hours) {
        if (day >= 10) { return true }
        }

    for (let i = 0; i < hours.length - 2; i++) {
        if (hours.slice(i, i + 3).reduce((a, b) => a + b, 0) / 3 >= 8) { return true}
    }

    return false;
}


console.log(tooMuchScreenTime([1, 2, 3, 4, 5, 6, 7]));
console.log(tooMuchScreenTime([7, 8, 8, 4, 2, 2, 3]));
console.log(tooMuchScreenTime([5, 6, 6, 6, 6, 6, 6]));
console.log(tooMuchScreenTime([1, 2, 3, 11, 1, 3, 4]));
console.log(tooMuchScreenTime([1, 2, 3, 10, 2, 1, 0]));
console.log(tooMuchScreenTime([3, 3, 5, 8, 8, 9, 4]));
console.log(tooMuchScreenTime([3, 9, 4, 8, 5, 7, 6]));
