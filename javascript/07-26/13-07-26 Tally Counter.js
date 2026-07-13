/*
Tally Counter
Given a string of tally marks, return the total count represented.

- Each pipe "|" represents one count.
- Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
- Groups are separated by a space.

1. getTallyCount("||||") should return 4.
2. getTallyCount("||||/") should return 5.
3. getTallyCount("||||/ |||") should return 8.
4. getTallyCount("||||/ ||||/ ||||/ ||") should return 17.
5. getTallyCount("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |") should return 41.
 */

function getTallyCount(str) {
    const tallyArr = str.split(" ");

    return (tallyArr.length - 1) * 5 + tallyArr[tallyArr.length - 1].length;
}


console.log(getTallyCount("||||"));
console.log(getTallyCount("||||/"));
console.log(getTallyCount("||||/ |||"));
console.log(getTallyCount("||||/ ||||/ ||||/ ||"));
console.log(getTallyCount("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"));
