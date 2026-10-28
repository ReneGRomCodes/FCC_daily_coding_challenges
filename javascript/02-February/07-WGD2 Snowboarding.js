/*
2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

A snowboarder's stance is either "Regular" or "Goofy".
Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise
rotation.
The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".

1. get_landing_stance("Regular", 90) should return "Regular".
2. get_landing_stance("Regular", 180) should return "Goofy".
3. get_landing_stance("Goofy", -270) should return "Regular".
4. get_landing_stance("Regular", 2340) should return "Goofy".
5. get_landing_stance("Goofy", 2160) should return "Goofy".
6. get_landing_stance("Goofy", -540) should return "Regular".
 */

function getLandingStance(startStance, rotation) {
    const isFlipped = (Math.floor(Math.abs(rotation) / 180)) % 2 !== 0;

    if (isFlipped) {
        return startStance === "Regular" ? "Goofy" : "Regular";
    }

    return startStance;
}


console.log(getLandingStance("Regular", 90));
console.log(getLandingStance("Regular", 180));
console.log(getLandingStance("Goofy", -270));
console.log(getLandingStance("Regular", 2340));
console.log(getLandingStance("Goofy", 2160));
console.log(getLandingStance("Goofy", -540));
