"""
Message Decoder
Given a secret message string, and an integer representing the number of letters that were used to shift the message to
encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.

1. decode("Xlmw mw e wigvix qiwweki.", 4) should return "This is a secret message."
2. decode("Byffi Qilfx!", 20) should return "Hello World!"
3. decode("Zqd xnt njzx?", -1) should return "Are you okay?"
4. decode("oannLxmnLjvy", 9) should return "freeCodeCamp"
"""

def decode(message: str, shift: int) -> str:
    decoded: str = ""

    for char in message:
        if char.isalpha():
            # pick base depending on case.
            base: int = ord('A') if char.isupper() else ord('a')
            # shift within 0–25 range, wrapping around.
            decoded += chr((ord(char) - base - shift) % 26 + base)
        else:
            decoded += char

    return decoded


print(decode("Xlmw mw e wigvix qiwweki.", 4))
print(decode("Byffi Qilfx!", 20))
print(decode("Zqd xnt njzx?", -1))
print(decode("oannLxmnLjvy", 9))
