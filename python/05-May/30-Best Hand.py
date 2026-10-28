"""
Best Hand
Given an array of five strings representing playing cards, return the name of the best hand.

- Each card is represented as a two-character string: the rank followed by the suit, "2h" for example.
  - Ranks, from low to high, are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
  - Suits are: "h", "d", "c", and "s".
- Aces ("A") can be used as high or low in a straight.

The hands, in order from worst to best, are:

Name	            Description
"High Card"	        No pair or better
"Pair"	            Two of one rank
"Two Pair"	        Two of one rank and two of another
"Three of a Kind"	Three of one rank
"Straight"	        Five ranks in a row
"Flush"	            Five of the same suit
"Full House"	    Three of one rank, and two of another
"Four of a Kind"	Four of one rank
"Straight Flush"	Five ranks in a row of the same suit
"Royal Flush"	    "A", "K", "Q", "J", "T" of the same suit

Return the name of the best hand.

1. get_best_hand(["7s", "7h", "7d", "2c", "5h"]) should return "Three of a Kind".
2. get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]) should return "Full House".
3. get_best_hand(["2h", "5h", "7h", "9h", "Jh"]) should return "Flush".
4. get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]) should return "Four of a Kind".
5. get_best_hand(["Ts", "Th", "9d", "9c", "8h"]) should return "Two Pair".
6. get_best_hand(["9c", "8c", "7c", "6c", "5c"]) should return "Straight Flush".
7. get_best_hand(["As", "Kh", "Jd", "8c", "5h"]) should return "High Card".
8. get_best_hand(["As", "2h", "3d", "4c", "5h"]) should return "Straight".
9. get_best_hand(["Ts", "Th", "7c", "6d", "5h"]) should return "Pair".
10. get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]) should return "Royal Flush".
"""


def get_best_hand(cards: list[str]) -> str:
    rank_values: dict[str, int] = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
                                   "Q": 12, "K": 13, "A": 14}

    ranks: list[int] = sorted([rank_values[card[0]] for card in cards])
    suits: set[str] = set([card[1] for card in cards])

    # Count frequencies.
    counts: dict[int, int] = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    freq: list[int] = sorted(counts.values(), reverse=True)

    # Check flush.
    is_flush: bool = len(suits) == 1

    # Check straight.
    is_straight: bool = False
    is_royal: bool = False
    if len(set(ranks)) == 5:
        if ranks[-1] - ranks[0] == 4:
            is_straight = True
            if ranks[0] == 10:
                is_royal = True
        elif ranks == [2, 3, 4, 5, 14]:  # Low Ace
            is_straight = True

    # Evaluate from best to worst.
    if is_straight and is_flush and is_royal: return "Royal Flush"
    if is_straight and is_flush: return "Straight Flush"
    if freq[0] == 4: return "Four of a Kind"
    if freq[0] == 3 and freq[1] == 2: return "Full House"
    if is_flush: return "Flush"
    if is_straight: return "Straight"
    if freq[0] == 3: return "Three of a Kind"
    if freq[0] == 2 and freq[1] == 2: return "Two Pair"
    if freq[0] == 2: return "Pair"

    return "High Card"


print(get_best_hand(["7s", "7h", "7d", "2c", "5h"]))
print(get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]))
print(get_best_hand(["2h", "5h", "7h", "9h", "Jh"]))
print(get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]))
print(get_best_hand(["Ts", "Th", "9d", "9c", "8h"]))
print(get_best_hand(["9c", "8c", "7c", "6c", "5c"]))
print(get_best_hand(["As", "Kh", "Jd", "8c", "5h"]))
print(get_best_hand(["As", "2h", "3d", "4c", "5h"]))
print(get_best_hand(["Ts", "Th", "7c", "6d", "5h"]))
print(get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]))
