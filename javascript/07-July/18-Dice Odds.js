/*
Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format
"1 in X".

- The number of dice will be between 1 and 6.
- The target sum is always achievable with the given number of dice.
- Round "X" to the nearest whole number.

1. get_odds(1, 5) should return "1 in 6".
2. get_odds(2, 4) should return "1 in 12".
3. get_odds(3, 10) should return "1 in 8".
4. get_odds(4, 7) should return "1 in 65".
5. get_odds(5, 26) should return "1 in 111".
6. get_odds(6, 35) should return "1 in 7776".
 */

function getOdds(dice, target) {
    let ways = new Array(37).fill(0);
    ways[0] = 1;

    for (let i = 0; i < dice; i++) {
        let nextWays = new Array(37).fill(0);

        for (let currentSum = 0; currentSum < 37; currentSum++) {
            if (ways[currentSum] > 0) {

                for (let face = 1; face <= 6; face++) {
                    if (currentSum + face <= 36) {
                        nextWays[currentSum + face] += ways[currentSum];
                    }
                }
            }
        }
        ways = nextWays;
    }

    const totalOutcomes = Math.pow(6, dice);
    const waysToWin = ways[target];
    const x = Math.round(totalOutcomes / waysToWin);

    return `1 in ${x}`;
}


console.log(getOdds(1, 5));
console.log(getOdds(2, 4));
console.log(getOdds(3, 10));
console.log(getOdds(4, 7));
console.log(getOdds(5, 26));
console.log(getOdds(6, 35));
