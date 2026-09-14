/*
Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an,
and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.

1. build_acronym("Search Engine Optimization") should return "SEO".
2. build_acronym("Frequently Asked Questions") should return "FAQ".
3. build_acronym("National Aeronautics and Space Administration") should return "NASA".
4. build_acronym("Federal Bureau of Investigation") should return "FBI".
5. build_acronym("For your information") should return "FYI".
6. build_acronym("By the way") should return "BTW".
7. build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily")
    should return "AUHWPOTIMSH".
 */

function buildAcronym(str) {

    return str;
}


console.log(buildAcronym("Search Engine Optimization"));
console.log(buildAcronym("Frequently Asked Questions"));
console.log(buildAcronym("National Aeronautics and Space Administration"));
console.log(buildAcronym("Federal Bureau of Investigation"));
console.log(buildAcronym("For your information"));
console.log(buildAcronym("By the way"));
console.log(buildAcronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"));
