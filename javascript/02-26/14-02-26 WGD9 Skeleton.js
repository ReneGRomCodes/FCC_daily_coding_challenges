/*
2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment

Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200

1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy".
 */

function getDifficulty(track) {
    let points = 0;

    for (let i = 0; i < track.length; i++) {
        const hasCurve = track[i] === "L" || track[i] === "R";
        const hasDirectionChange =
            i !== 0 && (
            (track[i] === "L" && track[i - 1] === "R") || (track[i] === "R" && track[i - 1] === "L")
            );

        if (hasDirectionChange) {
            points += 15;
        } else if (hasCurve) {
            points += 5;
        }
    }

    if (points <= 100) {
        return "Easy";
    } else if (points <= 200) {
        return "Medium";
    } else {
        return "Hard";
    }
}


console.log(getDifficulty("SLSLLSRRLSRLRL"));
console.log(getDifficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"));
console.log(getDifficulty("SRRRRLSLLRLRSSRLSRL"));
console.log(getDifficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"));
console.log(getDifficulty("SLLSSLRLSLSLRSLSSLRL"));
console.log(getDifficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"));
