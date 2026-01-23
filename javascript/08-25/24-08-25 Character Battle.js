/*
Character Battle
Given two strings representing your army and an opposing army, each character from your army battles the character at
the same position from the opposing army using the following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles.

1. battle("Hello", "World") should return "We lost".
2. battle("pizza", "salad") should return "We won".
3. battle("C@T5", "D0G$") should return "We won".
4. battle("kn!ght", "orc") should return "Opponent retreated".
5. battle("PC", "Mac") should return "We retreated".
6. battle("Wizards", "Dragons") should return "It was a tie".
7. battle("Mr. Smith", "Dr. Jones") should return "It was a tie".
 */

function getStrength(character) {
    if (character >= 'a' && character <= 'z') {
        return character.charCodeAt(0) - 96;
    } else if (character >= 'A' && character <= 'Z') {
        return character.charCodeAt(0) - 38;
    } else if (character >= '0' && character <= '9') {
        return parseInt(character, 10);
    } else {
        return 0;
    }
}


function battle(myArmy, opposingArmy) {
    let myWins = 0;
    let opposingWins = 0;

    // Compare army sizes.
    if (myArmy.length > opposingArmy.length) {
        return "Opponent retreated"
    } else if (opposingArmy.length > myArmy.length) {
        return "We retreated"
    }

    // Battle!
    for (let i=0; i < myArmy.length; i++) {
        const myCharStrength = getStrength(myArmy[i]);
        const opposingCharStrength = getStrength(opposingArmy[i]);

        if (myCharStrength > opposingCharStrength) {
            myWins++
        } else if (myCharStrength < opposingCharStrength) {
            opposingWins++
        }
    }

    if (myWins > opposingWins) {
        return "We won"
    } else if (myWins < opposingWins) {
        return "We lost"
    } else {
        return "It was a tie"
    }
}


console.log(battle("Hello", "World"));
console.log(battle("pizza", "salad"));
console.log(battle("C@T5", "D0G$"));
console.log(battle("kn!ght", "orc"));
console.log(battle("PC", "Mac"));
console.log(battle("Wizards", "Dragons"));
console.log(battle("Mr. Smith", "Dr. Jones"));
