/*
2026 Winter Games Day 15: Freestyle Skiing
Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid
second words.

The two words will be separated by a single space.

Valid first words:
"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"

Valid second words:
"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"

1. is_valid_trick("Polar Vortex") should return True.
2. is_valid_trick("Solar Icequake") should return True.
3. is_valid_trick("Thunder Blizzard") should return True.
4. is_valid_trick("Phantom Frostbite") should return True.
5. is_valid_trick("Ghost Avalanche") should return True.
6. is_valid_trick("Snowstorm Shadow") should return False.
7. is_valid_trick("Solar Sky") should return False.
 */

function isValidTrick(trickName) {
    const validFirstWords = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"];
    const validSecondWords = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"];
    const trickNameArr = trickName.split(" ");

    return validFirstWords.includes(trickNameArr[0]) && validSecondWords.includes(trickNameArr[1]);
}


console.log(isValidTrick("Polar Vortex"));
console.log(isValidTrick("Solar Icequake"));
console.log(isValidTrick("Thunder Blizzard"));
console.log(isValidTrick("Phantom Frostbite"));
console.log(isValidTrick("Ghost Avalanche"));
console.log(isValidTrick("Snowstorm Shadow"));
console.log(isValidTrick("Solar Sky"));
