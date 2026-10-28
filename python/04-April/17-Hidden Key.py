"""
Hidden Key
Welcome to the 250th daily challenge!

Given an encoded string, decode it using an encryption key and return it.

To find the key:
- Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
- Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a
  non-letter, find its first letter.

To decode the message, go over each letter in the encoded message and:
- Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
- Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
- Shift the encoded letter backward in the alphabet by that number.
- If the shift goes before "A", wrap around to "Z".

For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get
"C". Repeat this process for each letter to decode the full message.

- Only letters are shifted, spaces are returned as-is.
- All given and returned letters are uppercase.

1. decode("YAVJYNXE") should return "CONGRATS".
2. decode("YALLUT PQUMJP") should return "CODING LEGEND".
3. decode("UAC DYR EISAKYM") should return "YOU ARE AWESOME".
4. decode("GQMS NBMZU") should return "KEEP GOING".
5. decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB") should return "A WINNER IS A DREAMER WHO NEVER GIVES UP".
"""

def decode(message: str) -> str:
    key: str = "VLHCGMDLNH"
    result: list[str] = []

    key_index: int = 0

    for char in message:
        if char == " ":
            result.append(" ")
            continue

        key_char: str = key[key_index % len(key)]
        shift: int = ord(key_char) - ord('A') + 1

        new_pos: int = (ord(char) - ord('A') - shift) % 26
        decoded_char: str = chr(new_pos + ord('A'))

        result.append(decoded_char)
        key_index += 1

    return "".join(result)


print(decode("YAVJYNXE"))
print(decode("YALLUT PQUMJP"))
print(decode("UAC DYR EISAKYM"))
print(decode("GQMS NBMZU"))
print(decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"))
