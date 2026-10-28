/*
Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the
average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.
1. mile_pace(3, "24:00") should return "08:00".
2. mile_pace(1, "06:45") should return "06:45".
3. mile_pace(2, "07:00") should return "03:30".
4. mile_pace(26.2, "120:35") should return "04:36".
 */

function milePace(miles, duration) {
    const durationList = duration.split(":");
    const avrgMilePaceSec = (Math.floor(durationList[0]) * 60 + Math.floor(durationList[1])) / miles;
    const avrgMilePace =
        `${Math.floor(avrgMilePaceSec / 60)
            .toString()
            .padStart(2, '0')}:` +
        `${Math.floor(avrgMilePaceSec % 60)
            .toString()
            .padStart(2, '0')}`;


    return avrgMilePace;
}


console.log(milePace(3, "24:00"));
console.log(milePace(1, "06:45"));
console.log(milePace(2, "07:00"));
console.log(milePace(26.2, "120:35"));
