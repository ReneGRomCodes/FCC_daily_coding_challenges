/*
2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0

Return:
"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25

1. get_hill_rating(95, 900, "Slalom") should return "Green".
2. get_hill_rating(620, 2800, "Downhill") should return "Black".
3. get_hill_rating(420, 1680, "Giant Slalom") should return "Blue".
4. get_hill_rating(250, 3000, "Downhill") should return "Green".
5. get_hill_rating(110, 900, "Slalom") should return "Blue".
6. get_hill_rating(380, 1500, "Giant Slalom") should return "Black".
 */

function getHillRating(drop, distance, type) {
    const typeMult = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0,
    };

    const steepness = drop / distance * typeMult[type];

    if (steepness <= 0.1) {
        return "Green";
    } else if (steepness <= 0.25) {
        return "Blue";
    } else {
        return "Black";
    }
}


console.log(getHillRating(95, 900, "Slalom"));
console.log(getHillRating(620, 2800, "Downhill"));
console.log(getHillRating(420, 1680, "Giant Slalom"));
console.log(getHillRating(250, 3000, "Downhill"));
console.log(getHillRating(110, 900, "Slalom"));
console.log(getHillRating(380, 1500, "Giant Slalom"));
