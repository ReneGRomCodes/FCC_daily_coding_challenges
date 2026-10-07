/*
Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following
strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.

1. can_post("Hello world") should return "short post".
2. can_post("This is a longer message but still under eighty characters.") should return "long post".
3. can_post("This message is too long to fit into either of the character limits for a social media post.")
    should return "invalid post".
 */

function canPost(message) {

    return message;
}


console.log(canPost("Hello world"));
console.log(canPost("This is a longer message but still under eighty characters."));
console.log(canPost("This message is too long to fit into either of the character limits for a social media post."));
