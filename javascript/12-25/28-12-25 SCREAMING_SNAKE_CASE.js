/*
SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)

1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
3. to_screaming_snake_case("user_id") should return "USER_ID".
4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
5. to_screaming_snake_case("username") should return "USERNAME".
 */

function toScreamingSnakeCase(variableName) {

    return variableName;
}


console.log(toScreamingSnakeCase("userEmail"));
console.log(toScreamingSnakeCase("UserPassword"));
console.log(toScreamingSnakeCase("user_id"));
console.log(toScreamingSnakeCase("user-address"));
console.log(toScreamingSnakeCase("username"));
