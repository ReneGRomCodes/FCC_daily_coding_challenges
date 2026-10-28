/*
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
 */


function getBestHand(hand) {
    // Set up our dictionaries and arrays.
    const rankValues = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 };
    const ranks = [];
    const suits = new Set();
    const counts = {};

    // Parse the input array.
    for (const card of hand) {
        const rank = rankValues[card[0]];
        ranks.push(rank);
        suits.add(card[1]);
        counts[rank] = (counts[rank] || 0) + 1;
    }

    // Sort ranks for sequence checking.
    ranks.sort((a, b) => a - b);

    // Check for Sequence (Straights) & Categories (Flushes).
    const isFlush = suits.size === 1;
    let isStraight = false;
    let isRoyal = false;

    // A straight needs 5 unique cards.
    if (new Set(ranks).size === 5) {
        // Standard straight (e.g., 4, 5, 6, 7, 8).
        if (ranks[4] - ranks[0] === 4) {
            isStraight = true;
            if (ranks[0] === 10) isRoyal = true; // Starts with 10 (10, J, Q, K, A).
        }
        // Special case: Low Ace Straight (A, 2, 3, 4, 5 -> values 2, 3, 4, 5, 14).
        else if (ranks.join(',') === '2,3,4,5,14') {
            isStraight = true;
        }
    }

    // Check for Frequencies (Pairs, 3-of-a-kind, etc.).
    // Sort frequencies highest to lowest.
    const frequencies = Object.values(counts).sort((a, b) => b - a);

    // Return the highest ranking hand.
    if (isStraight && isFlush && isRoyal) return "Royal Flush";
    if (isStraight && isFlush) return "Straight Flush";
    if (frequencies[0] === 4) return "Four of a Kind";
    if (frequencies[0] === 3 && frequencies[1] === 2) return "Full House";
    if (isFlush) return "Flush";
    if (isStraight) return "Straight";
    if (frequencies[0] === 3) return "Three of a Kind";
    if (frequencies[0] === 2 && frequencies[1] === 2) return "Two Pair";
    if (frequencies[0] === 2) return "Pair";

    return "High Card";
}


console.log(getBestHand(["7s", "7h", "7d", "2c", "5h"]));
console.log(getBestHand(["Ks", "Kh", "Kd", "4s", "4h"]));
console.log(getBestHand(["2h", "5h", "7h", "9h", "Jh"]));
console.log(getBestHand(["As", "Ah", "Ad", "Ac", "Kh"]));
console.log(getBestHand(["Ts", "Th", "9d", "9c", "8h"]));
console.log(getBestHand(["9c", "8c", "7c", "6c", "5c"]));
console.log(getBestHand(["As", "Kh", "Jd", "8c", "5h"]));
console.log(getBestHand(["As", "2h", "3d", "4c", "5h"]));
console.log(getBestHand(["Ts", "Th", "7c", "6d", "5h"]));
console.log(getBestHand(["As", "Ks", "Qs", "Js", "Ts"]));
