/*
Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up,
determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.

Return:
- "early" if you woke up before your alarm time.
- "on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
- "late" if you woke up more than 10 minutes after your alarm time.

Both times are on the same day.

1. alarm_check("07:00", "06:45") should return "early".
2. alarm_check("06:30", "06:30") should return "on time".
3. alarm_check("08:10", "08:15") should return "on time".
4. alarm_check("09:30", "09:45") should return "late".
5. alarm_check("08:15", "08:25") should return "on time".
6. alarm_check("05:45", "05:56") should return "late".
7. alarm_check("04:30", "04:00") should return "early".
 */

function alarmCheck(alarmTime, wakeTime) {
    const alarmArr = alarmTime.split(":");
    const wakeArr = wakeTime.split(":");
    const alarmTotalMinutes = Number(alarmArr[0]) * 60 + Number(alarmArr[1]);
    const wakeTotalMinutes = Number(wakeArr[0]) * 60 + Number(wakeArr[1]);

    if (wakeTotalMinutes < alarmTotalMinutes) {
        return "early";
    } else if (wakeTotalMinutes <= alarmTotalMinutes + 10) {
        return "on time"
    } else {
        return "late";
    }
}


console.log(alarmCheck("07:00", "06:45"));
console.log(alarmCheck("06:30", "06:30"));
console.log(alarmCheck("08:10", "08:15"));
console.log(alarmCheck("09:30", "09:45"));
console.log(alarmCheck("08:15", "08:25"));
console.log(alarmCheck("05:45", "05:56"));
console.log(alarmCheck("04:30", "04:00"));
