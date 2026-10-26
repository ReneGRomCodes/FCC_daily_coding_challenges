/*
Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each
line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

*
 *
*
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 **
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

1. generate_snowflake("* \n *\n* ") should return "*  *\n ** \n*  *".
2. generate_snowflake("X=~") should return "X=~~=X".
3. generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ") should return " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ".
4. generate_snowflake("*   *\n * * \n* * *\n * * \n*   *")
    should return "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *".
5. generate_snowflake("*  -\n * -\n*  -") should return "*  --  *\n * -- * \n*  --  *".
 */

function generateSnowflake(crystals) {
    const crystalsArr = crystals.split("\n");
    const revCrystals = crystalsArr.map(x => x.split("").reverse().join(""));
    const snowflake = [];

    for (let i = 0; i < crystalsArr.length; i++) {
        const a = crystalsArr[i];
        const b = revCrystals[i];

        if (i !== crystalsArr.length - 1) { snowflake.push(`${a}${b}\n`) }
        else { snowflake.push(`${a}${b}`) }
    }

    return snowflake.join("");
}


console.log(generateSnowflake("* \n *\n* "));
console.log(generateSnowflake("X=~"));
console.log(generateSnowflake(" X  \n  v \nX--=\n  ^ \n X  "));
console.log(generateSnowflake("*   *\n * * \n* * *\n * * \n*   *"));
console.log(generateSnowflake("*  -\n * -\n*  -"));
