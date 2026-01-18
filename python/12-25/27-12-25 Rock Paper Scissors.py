"""
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
"""

def rock_paper_scissors(player1: str, player2: str) -> str:
    win_lose = {  # Value at '0' loses, '1' wins.
        "Rock": ("Scissors", "Paper"),
        "Paper": ("Rock", "Scissors"),
        "Scissors": ("Paper", "Rock"),
    }

    if player1 == win_lose[player2][0]:
        return "Player 2 wins"
    elif player1 == win_lose[player2][1]:
        return "Player 1 wins"

    return "Tie"


print(rock_paper_scissors("Rock", "Rock"))
print(rock_paper_scissors("Rock", "Paper"))
print(rock_paper_scissors("Scissors", "Paper"))
print(rock_paper_scissors("Rock", "Scissors"))
print(rock_paper_scissors("Scissors", "Scissors"))
print(rock_paper_scissors("Scissors", "Rock"))
