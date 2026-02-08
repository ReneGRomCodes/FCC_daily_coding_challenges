/*
2026 Winter Games Day 3: Biathlon
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon,
return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.

1. calculate_penalty_distance([4, 4]) should return 300.
2. calculate_penalty_distance([5, 5]) should return 0.
3. calculate_penalty_distance([4, 5, 3, 5]) should return 450.
4. calculate_penalty_distance([5, 4, 5, 5]) should return 150.
5. calculate_penalty_distance([4, 3, 0, 3]) should return 1500.
 */

function calculatePenaltyDistance(rounds) {
    const targetsHit = rounds.reduce((a, b) => a + b);

    return (rounds.length * 5 - targetsHit) * 150;
}


console.log(calculatePenaltyDistance([4, 4]));
console.log(calculatePenaltyDistance([5, 5]));
console.log(calculatePenaltyDistance([4, 5, 3, 5]));
console.log(calculatePenaltyDistance([5, 4, 5, 5]));
console.log(calculatePenaltyDistance([4, 3, 0, 3]));
