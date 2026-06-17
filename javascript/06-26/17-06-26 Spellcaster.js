/*
Spellcaster
Given a string of spell codes you are casting, calculate the total score.

Each character in the string represents a spell:

Code	Spell	    Category	    Base Score
"f"	    Fire	    Destruction	    3
"l"	    Lightning	Destruction	    3
"i"	    Ice	        Control	        2
"w"	    Wind	    Control	        2
"h"	    Heal	    Restoration	    1
"s"	    Shield	    Restoration	    1

A combo multiplier is applied based on how many spells in a row have been cast from different categories:

- The first spell always scores at base value.
- Each consecutive spell from a different category than the previous increases the multiplier by 1.
- Casting a spell from the same category as the previous resets the multiplier back to 1.
- The score for each spell is its base score multiplied by the current multiplier.

Return the total score from the sequence of spells.

1. cast("fihwl") should return 33.
2. cast("lwswfi") should return 45.
3. cast("wislhfl") should return 37.
4. cast("sihwlih") should return 50.
5. cast("wishlfihwslwifihl") should return 101.
 */

function cast(spells) {
    const spellsObj = {
        f: ["Destruction", 3],
        l: ["Destruction", 3],
        i: ["Control", 2],
        w: ["Control", 2],
        h: ["Restoration", 1],
        s: ["Restoration", 1],
    };
    let currentCat = spellsObj[spells[0]][0];
    let multiplier = 1;
    let totalScore = 0;

    for (let i = 0; i < spells.length; i++) {
        const spellCat = spellsObj[spells[i]][0];
        const spellScore = spellsObj[spells[i]][1];

        if (spellCat !== currentCat) {
            multiplier += 1;
            currentCat = spellCat;
        } else {
            multiplier = 1;
        }

        totalScore += spellScore * multiplier;
    }

    return totalScore;
}


console.log(cast("fihwl"));
console.log(cast("lwswfi"));
console.log(cast("wislhfl"));
console.log(cast("sihwlih"));
console.log(cast("wishlfihwslwifihl"));
