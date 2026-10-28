/*
String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end
of it.

1. mirror("freeCodeCamp") should return "freeCodeCamppmaCedoCeerf".
2. mirror("RaceCar") should return "RaceCarraCecaR".
3. mirror("helloworld") should return "helloworlddlrowolleh".
4. mirror("The quick brown fox...") should return "The quick brown fox......xof nworb kciuq ehT".
 */

function mirror(str) {
    return str + str.split("").reverse().join("");
}


console.log(mirror("freeCodeCamp"));
console.log(mirror("RaceCar"));
console.log(mirror("helloworld"));
console.log(mirror("The quick brown fox..."));
