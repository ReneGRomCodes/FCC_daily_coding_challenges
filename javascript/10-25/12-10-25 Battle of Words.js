/*
Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding
word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.

Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number
of wins.
1. battle("hello world", "hello word") should return "We win".
2. battle("Hello world", "hello world") should return "We win".
3. battle("lorem ipsum", "kitty ipsum") should return "We lose".
4. battle("hello world", "world hello") should return "Draw".
5. battle("git checkout", "git switch") should return "We win".
6. battle("Cheeseburger with fries", "Cheeseburger with Fries") should return "We lose".
7. battle("We must never surrender", "Our team must win") should return "Draw".
 */

function getLetterValue(letter) {
    let value = parseInt(letter, 36) - 9;

    if (/[A-Z]/.test(letter)) { value *= 2 }

    return value;
}


function battle(ourTeam, opponent) {
    const ourArr = ourTeam.split(" ");
    const oppArr = opponent.split(" ");
    let ourTeamScore = 0;
    let opponentScore = 0;

    for (let i = 0; i < oppArr.length; i++) {
        let ourWordScore = ourArr[i].split("").reduce((sum, x) => sum + getLetterValue(x), 0);
        let oppWordScore = oppArr[i].split("").reduce((sum, x) => sum + getLetterValue(x), 0);

        if (ourWordScore > oppWordScore) { ourTeamScore++ }
        else if (ourWordScore < oppWordScore) { opponentScore++ }
    }

    if (ourTeamScore > opponentScore) { return "We win" }
    else if (ourTeamScore < opponentScore) { return "We lose" }
    else { return "Draw" }
}


console.log(battle("hello world", "hello word"));
console.log(battle("Hello world", "hello world"));
console.log(battle("lorem ipsum", "kitty ipsum"));
console.log(battle("hello world", "world hello"));
console.log(battle("git checkout", "git switch"));
console.log(battle("Cheeseburger with fries", "Cheeseburger with Fries"));
console.log(battle("We must never surrender", "Our team must win"));
