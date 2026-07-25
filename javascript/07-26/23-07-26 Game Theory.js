/*
Game Theory
Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].

- The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
- Each character represents one round, scored as follows:
  - If both players cooperate, each scores 3.
  - If both players defect, each scores 1.
  - If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.

1. play_game("CCCC", "CCCC") should return [12, 12].
2. play_game("DDDD", "DDDD") should return [4, 4].
3. play_game("CCDD", "CDDD") should return [5, 10].
4. play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD") should return [24, 34].
5. play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC") should return [66, 21].
 */

function playGame(p1, p2) {
    let score = [0, 0];

    for (let i = 0; i < p1.length; i++) {
        const isP1Coop = p1[i] === "C";
        const isP2Coop = p2[i] === "C";

        if (isP1Coop && isP2Coop) {
            score[0] += 3;
            score[1] += 3;
        } else if (!isP1Coop && !isP2Coop) {
            score[0] += 1;
            score[1] += 1;
        } else {
            if (isP1Coop) {
                score[1] += 5;
            } else {
                score[0] += 5;
            }
        }
    }

    return score;
}


console.log(playGame("CCCC", "CCCC"));
console.log(playGame("DDDD", "DDDD"));
console.log(playGame("CCDD", "CDDD"));
console.log(playGame("CCCDCDCCCDDC", "CCDDCDCDDCCD"));
console.log(playGame("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"));
