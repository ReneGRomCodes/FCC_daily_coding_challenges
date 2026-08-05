/*
Spoken Duration
Given a number of seconds, return the duration in spoken English.

- Break the duration into hours, minutes, and seconds.
- Skip any zero values.
- Use singular or plural as appropriate ("1 hour", "2 hours").
- If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes
  and 3 seconds").

1. get_spoken_duration(3723) should return "1 hour, 2 minutes and 3 seconds".
2. get_spoken_duration(7295) should return "2 hours, 1 minute and 35 seconds".
3. get_spoken_duration(8521) should return "2 hours, 22 minutes and 1 second".
4. get_spoken_duration(435) should return "7 minutes and 15 seconds".
5. get_spoken_duration(14455) should return "4 hours and 55 seconds".
6. get_spoken_duration(72000) should return "20 hours".
7. get_spoken_duration(1) should return "1 second".
 */

function getSpokenDuration(seconds) {
    const timeUnits = {
        hour: Math.floor(seconds / 3600),
        minute: Math.floor((seconds % 3600) / 60),
        second: seconds % 60,
    };

    const spokenDurationList = [];

    for (const [key, value] of Object.entries(timeUnits)) {
        if (value) {
            spokenDurationList.push(`${value} ${key}`);
        }
        if (value > 1) {
            spokenDurationList[spokenDurationList.length - 1] += "s";
        }
    }

    if (spokenDurationList.length === 1) {
        return spokenDurationList[0];
    } else if (spokenDurationList.length === 2) {
        return spokenDurationList.join(" and ");
    } else {
        return `${spokenDurationList.slice(0, 2).join(", ")} and ${spokenDurationList[2]}`;
    }
}


console.log(getSpokenDuration(3723));
console.log(getSpokenDuration(7295));
console.log(getSpokenDuration(8521));
console.log(getSpokenDuration(435));
console.log(getSpokenDuration(14455));
console.log(getSpokenDuration(72000));
console.log(getSpokenDuration(1));
