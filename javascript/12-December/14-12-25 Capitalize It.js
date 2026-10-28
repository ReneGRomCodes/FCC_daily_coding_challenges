/*
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.

1. title_case("hello world") should return "Hello World".
2. title_case("the quick brown fox") should return "The Quick Brown Fox".
3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
 */

function titleCase(title) {
    return title.split(" ")
        .map(word => word[0].toUpperCase() + word.slice(1).toLowerCase())
        .join(" ");
}


console.log(titleCase("hello world"));
console.log(titleCase("the quick brown fox"));
console.log(titleCase("JAVASCRIPT AND PYTHON"));
console.log(titleCase("AvOcAdO tOAst fOr brEAkfAst"));
