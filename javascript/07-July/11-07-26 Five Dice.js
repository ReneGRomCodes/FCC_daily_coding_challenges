/*
Five Dice
Given an array of five dice with values 1-6, return the best possible hand.

Here are the hands ranked lowest to highest:

Hand	            Description
"no pair"	        No pair or better
"pair"	            Two dice with the same value
"two pair"	        Two different pairs
"three of a kind"	Three dice with the same value
"small straight"	Four consecutive values
"large straight"	Five consecutive values
"full house"	    Three of a kind and a pair
"four of a kind"	Four dice with the same value
"five of a kind"	All five dice with the same value

1. five_dice([1, 1, 1, 1, 1]) should return "five of a kind".
2. five_dice([5, 5, 5, 6, 5]) should return "four of a kind".
3. five_dice([2, 5, 6, 4, 3]) should return "large straight".
4. five_dice([4, 3, 3, 3, 1]) should return "three of a kind".
5. five_dice([4, 6, 2, 6, 5]) should return "pair".
6. five_dice([1, 4, 5, 6, 2]) should return "no pair".
7. five_dice([1, 3, 4, 6, 2]) should return "small straight".
8. five_dice([2, 2, 5, 2, 5]) should return "full house".
9. five_dice([6, 4, 5, 6, 4]) should return "two pair".
 */

const fiveDice = (dice) => {
    // Build histogram of 'dice'.
    const hist = {};
    for (const n of dice) {
        hist[n] = (hist[n] || 0) + 1;
    }

    const counts = Object.values(hist);
    const uniqueKeys = Object.keys(hist);
    const uniqueCount = uniqueKeys.length;

    // Check for straights by sorting unique numbers and turn them into a single string.
    uniqueKeys.sort((a, b) => a - b);
    const straightStr = uniqueKeys.join("");

    if (straightStr === "12345" || straightStr === "23456") {
        return "large straight";
    }

    if (straightStr.includes("1234") || straightStr.includes("2345") || straightStr.includes("3456")) {
        return "small straight";
    }

    // Further checks based on length of histogram length.
    if (uniqueCount === 1) return "five of a kind";

    if (uniqueCount === 2) {
        return counts.includes(4) ? "four of a kind" : "full house";
    }

    if (uniqueCount === 3) {
        return counts.includes(3) ? "three of a kind" : "two pair";
    }

    if (uniqueCount === 4) return "pair";

    return "no pair";
};


console.log(fiveDice([1, 1, 1, 1, 1]));
console.log(fiveDice([5, 5, 5, 6, 5]));
console.log(fiveDice([2, 5, 6, 4, 3]));
console.log(fiveDice([4, 3, 3, 3, 1]));
console.log(fiveDice([4, 6, 2, 6, 5]));
console.log(fiveDice([1, 4, 5, 6, 2]));
console.log(fiveDice([1, 3, 4, 6, 2]));
console.log(fiveDice([2, 2, 5, 2, 5]));
console.log(fiveDice([6, 4, 5, 6, 4]));
