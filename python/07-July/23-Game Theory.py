"""
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
"""

def play_game(p1: str, p2: str) -> list[int]:
    score: list[int] = [0, 0]

    for s1, s2 in zip(p1, p2):
        is_p1_coorp: bool = s1 == "C"
        is_p2_coorp: bool = s2 == "C"

        if is_p1_coorp and is_p2_coorp:
            score[0] += 3
            score[1] += 3
        elif not is_p1_coorp and not is_p2_coorp:
            score[0] += 1
            score[1] += 1
        else:
            if is_p1_coorp:
                score[1] += 5
            else:
                score[0] += 5

    return score


print(play_game("CCCC", "CCCC"))
print(play_game("DDDD", "DDDD"))
print(play_game("CCDD", "CDDD"))
print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))
print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))
