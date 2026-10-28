/*
Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:

All consonants should be converted to uppercase.
All vowels (a, e, i, o, u in any case) should be converted to lowercase.
All hyphens (-) should be converted to underscores (_).

1. to_consonant_case("helloworld") should return "HeLLoWoRLD".
2. to_consonant_case("HELLOWORLD") should return "HeLLoWoRLD".
3. to_consonant_case("_hElLO-WOrlD-") should return "_HeLLo_WoRLD_".
4. to_consonant_case("_~-generic_~-variable_~-name_~-here-~_") should return "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_".
 */

function toConsonantCase(str) {
    let cCase = "";

    for (let char of str) {
        if ("aeiou".includes(char.toLowerCase())) {
            cCase += char.toLowerCase();
        } else if (char === "-") {
            cCase += "_";
        } else {
            cCase += char.toUpperCase();
        }
    }

    return cCase;
}


console.log(toConsonantCase("helloworld"));
console.log(toConsonantCase("HELLOWORLD"));
console.log(toConsonantCase("_hElLO-WOrlD-"));
console.log(toConsonantCase("_~-generic_~-variable_~-name_~-here-~_"));
