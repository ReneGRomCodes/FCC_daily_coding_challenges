/*
Emoji Translator

Given a string of emojis, return the phrase using the following table:
Emoji	Word
👶	    "baby"
🐱	    "cat"
🐕	    "dog"
🐟	    "fish"
🥵	    "hot"
🧊	    "ice"
🪨	    "rock"
🦈	    "shark"
🍲	    "soup"
⭐	    "star"

Return the words separated by spaces.

1. get_emoji_phrase("🪨⭐") should return "rock star".
2. get_emoji_phrase("🥵🐕") should return "hot dog".
3. get_emoji_phrase("👶🦈") should return "baby shark".
4. get_emoji_phrase("⭐🐟") should return "star fish".
5. get_emoji_phrase("🧊🧊👶") should return "ice ice baby".
6. get_emoji_phrase("🐱🐟🍲") should return "cat fish soup".
 */

function getEmojiPhrase(str) {
    const emojiWord = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star",
    };
    const wordArr = [];

    for (const char of str) wordArr.push(emojiWord[char]);

    return wordArr.join(" ");
}


console.log(getEmojiPhrase("🪨⭐"));
console.log(getEmojiPhrase("🥵🐕"));
console.log(getEmojiPhrase("👶🦈"));
console.log(getEmojiPhrase("⭐🐟"));
console.log(getEmojiPhrase("🧊🧊👶"));
console.log(getEmojiPhrase("🐱🐟🍲"));
