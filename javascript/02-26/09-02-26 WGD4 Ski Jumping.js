/*
2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the
ski jump and determine if you won a medal or not.

Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:

165.5
172.0
158.0
180.0
169.5
175.0
162.0
170.0

If your score is the best, return "Gold"
If it's second best, return "Silver"
If it's third best, return "Bronze"
Otherwise, return "No Medal"

1. ski_jump_medal(125.0, 58.0, 0.0, 6.0) should return "Gold".
2. ski_jump_medal(119.0, 50.0, 1.0, 4.0) should return "Bronze".
3. ski_jump_medal(122.0, 52.0, -1.0, 4.0) should return "Silver".
4. ski_jump_medal(118.0, 50.5, -1.5, 4.0) should return "No Medal".
5. ski_jump_medal(124.0, 50.5, 2.0, 5.0) should return "Gold".
6. ski_jump_medal(119.0, 49.5, 0.0, 3.0) should return "No Medal".
 */

function skiJumpMedal(distancePoints, stylePoints, windComp, kPointBonus) {
    const TotalScore = [distancePoints, stylePoints, windComp, kPointBonus].reduce((a, b) => a + b);
    const scores = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0, TotalScore].sort().reverse();
    const rank = scores.indexOf(TotalScore);

    if (rank === 0) {
        return "Gold";
    } else if (rank === 1) {
        return "Silver";
    } else if (rank === 2) {
        return "Bronze";
    }

    return "No Medal";
}


console.log(skiJumpMedal(125.0, 58.0, 0.0, 6.0));
console.log(skiJumpMedal(119.0, 50.0, 1.0, 4.0));
console.log(skiJumpMedal(122.0, 52.0, -1.0, 4.0));
console.log(skiJumpMedal(118.0, 50.5, -1.5, 4.0));
console.log(skiJumpMedal(124.0, 50.5, 2.0, 5.0));
console.log(skiJumpMedal(119.0, 49.5, 0.0, 3.0));
