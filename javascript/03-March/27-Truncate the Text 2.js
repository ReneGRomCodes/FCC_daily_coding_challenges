/*
Truncate the Text 2
Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:
Letters	                    Width
"ilI"	                    1
"fjrt"	                    2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4

The table above includes all upper and lower case letters.

Additionally:
- Spaces (" ") have a width of 2
- Periods (".") have a width of 1
- If the given string is 50 units or less, return the string as-is, otherwise
- Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as
  close as possible to 50 units without going over.

1. truncate_text("The quick brown fox") should return "The quick brown f...".
2. truncate_text("The silky smooth sloth") should return "The silky smooth s...".
3. truncate_text("THE LOUD BRIGHT BIRD") should return "THE LOUD BRIG...".
4. truncate_text("The fast striped zebra") should return "The fast striped z...".
5. truncate_text("The big black bear") should return "The big black bear".
 */

function truncateText(str) {
    const charsWidth = {
        1: "ilI.",
        2: "fjrt ",
        3: "abcdeghkmnopqrstuvwxyzJL",
        4: "ABCDEFGHKMNOPQRSTUVWXYZ",
    };

    let widthS = 0;
    let truncatedS = "";

    for (let char of str) {
        for (const [width, chars] of Object.entries(charsWidth)) {
            if (chars.includes(char)) {
                const w = Number(width);

                // Reserve space for "...".
                if (widthS + w + 3 <= 50) {
                    widthS += w;
                    truncatedS += char;
                } else {
                    truncatedS += "...";
                    return truncatedS;
                }

                break;
            }
        }
    }

    return truncatedS;
}


console.log(truncateText("The quick brown fox"));
console.log(truncateText("The silky smooth sloth"));
console.log(truncateText("THE LOUD BRIGHT BIRD"));
console.log(truncateText("The fast striped zebra"));
console.log(truncateText("The big black bear"));
