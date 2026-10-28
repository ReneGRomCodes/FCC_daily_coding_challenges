/*
2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores
and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the
final score.

1. compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) should return 64.
2. compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) should return 80.
3. compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1) should return 67.
4. compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0) should return 67.5.
5. compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5) should return 59.
 */

function computeScore(judgeScores, ...penalties) {
    judgeScores.splice(judgeScores.indexOf(Math.max(...judgeScores)), 1);
    judgeScores.splice(judgeScores.indexOf(Math.min(...judgeScores)), 1);

    return judgeScores.reduce((a, b) => a + b) - penalties.reduce((a, b) => a + b, 0);
}


console.log(computeScore([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1));
console.log(computeScore([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));
console.log(computeScore([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1));
console.log(computeScore([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0));
console.log(computeScore([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5));
