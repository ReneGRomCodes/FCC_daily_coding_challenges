/*
Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match
of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.

1. rock_paper_scissors("Rock", "Rock") should return "Tie".
2. rock_paper_scissors("Rock", "Paper") should return "Player 2 wins".
3. rock_paper_scissors("Scissors", "Paper") should return "Player 1 wins".
4. rock_paper_scissors("Rock", "Scissors") should return "Player 1 wins".
5. rock_paper_scissors("Scissors", "Scissors") should return "Tie".
6. rock_paper_scissors("Scissors", "Rock") should return "Player 2 wins".
 */

function rockPaperScissors(player1, player2) {
    const winLose = {
        "Rock": ["Scissors", "Paper"],
        "Paper": ["Rock", "Scissors"],
        "Scissors": ["Paper", "Rock"]
    };

    if (player1 === winLose[player2][0]) { return "Player 2 wins" }
    else if (player1 === winLose[player2][1]) { return "Player 1 wins" }

    return "Tie";
}


console.log(rockPaperScissors("Rock", "Rock"));
console.log(rockPaperScissors("Rock", "Paper"));
console.log(rockPaperScissors("Scissors", "Paper"));
console.log(rockPaperScissors("Rock", "Scissors"));
console.log(rockPaperScissors("Scissors", "Scissors"));
console.log(rockPaperScissors("Scissors", "Rock"));
