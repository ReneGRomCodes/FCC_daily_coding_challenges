/*
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour
format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
1. to_12("1124") should return "11:24 AM".
2. to_12("0900") should return "9:00 AM".
3. to_12("1455") should return "2:55 PM".
4. to_12("2346") should return "11:46 PM".
5. to_12("0030") should return "12:30 AM".
 */

function to12(time) {
    let timeHours = Number (time.slice(0, 2));
    let timeMinutes = Number (time.slice(2));
    let suffix = "";

    if (timeHours > 12) {
        timeHours -= 12;
        suffix = "PM";
    } else if (timeHours === 12) {
        suffix = "PM";
    } else {
        if (timeHours === 0) {
            timeHours = 12;
        }
        suffix = "AM";
    }

    return `${timeHours}:${timeMinutes.toString().padStart(2, "0")} ${suffix}`;
}


console.log(to12("1124"));
console.log(to12("0900"));
console.log(to12("1455"));
console.log(to12("2346"));
console.log(to12("0030"));
