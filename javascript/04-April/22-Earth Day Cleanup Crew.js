/*
Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	     Base Value
"bottle"	    10
"can"	         6
"bag"	         8
"tire"	        35
"straw"	         4
"cardboard"	     3
"newspaper"	     3
"shoe"	        12
"electronics"	25
"battery"	    18
"mattress"	    38

A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

- Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
    - First consecutive occurrence: base value
    - Second: base value + 1
    - Third: base value + 2
    - etc.

- Fifth Item Multiplier: Every fifth item collected gets a multiplier.
    - Fifth item: *2
    - Tenth item: *3
    - etc.

Apply the multiplier after calculating any bonuses.

1. get_cleanup_score(["bottle", "straw", "shoe", "battery"]) should return 44.
2. get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) should return 58.
3. get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]) should return 79.
4. get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) should return 358.
5. get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can",
    "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"])
        should return 383.
 */

function getCleanupScore(items) {
    const itemScores = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    let streakCount = 1;
    let score = 0;

    for (let i = 0; i < items.length; i++) {
        const item = items[i];
        const isNormalItem = typeof item === "string" && item in itemScores;
        const isRareItem = typeof item === "object" && item[0] === "rare" && typeof item[1] === "number";
        const isStreak = i > 0 && items[i - 1] === item && !isRareItem;
        const applyFifthItemMultiplier = (i + 1) % 5 === 0;

        let itemScore = 0;

        if (isNormalItem) {
            itemScore += itemScores[item];
        } else if (isRareItem) {
            itemScore += item[1];
        } else {
            continue;  // Skip invalid items.
        }

        if (isStreak) {
            itemScore += streakCount;
            streakCount++;
        } else if (streakCount !== 1) {  // Reset streak count if streak is broken.
            streakCount = 1;
        }

        if (applyFifthItemMultiplier) {
            itemScore *= (i + 1) / 5 + 1;
        }

        score += itemScore
    }

    return score;
}


console.log(getCleanupScore(["bottle", "straw", "shoe", "battery"]));
console.log(getCleanupScore(["electronics", "straw", "newspaper", "bottle", "bag"]));
console.log(getCleanupScore(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]));
console.log(getCleanupScore(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]));
console.log(getCleanupScore(
    ["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle",
        ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]
));