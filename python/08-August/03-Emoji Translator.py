"""
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
"""

def get_emoji_phrase(s: str) -> str:
    emoji_word: dict[str, str] = {
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
    }

    return " ".join(emoji_word[emoji] for emoji in s)


print(get_emoji_phrase("🪨⭐"))
print(get_emoji_phrase("🥵🐕"))
print(get_emoji_phrase("👶🦈"))
print(get_emoji_phrase("⭐🐟"))
print(get_emoji_phrase("🧊🧊👶"))
print(get_emoji_phrase("🐱🐟🍲"))
