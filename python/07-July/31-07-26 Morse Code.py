"""
Morse Code

Given a Morse code string, return the decoded message using the following table:
Code	Letter	    Code	Letter
.-	    A	        -.	    N
-...	B	        ---	    O
-.-.	C	        .--.	P
-..	    D	        --.-	Q
.	    E	        .-.	    R
..-.	F	        ...	    S
--.	    G	        -	    T
....	H	        ..-	    U
..	    I	        ...-	V
.---	J	        .--	    W
-.-	    K	        -..-	X
.-..	L	        -.--	Y
--	    M	        --..	Z

- Letters are separated by a single space
- Words are separated by three spaces

1. decode_morse("--..") should return "Z".
2. decode_morse("... --- ...") should return "SOS".
3. decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--.") should return "FREECODECAMP".
4. decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") should return "HELLO WORLD".
5. decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.")
    should return "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG".
"""

MORSE_CODE: dict[str, str] = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
                              "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
                              "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
                              "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}


def decode_morse(code: str) -> str:
    decoded_words: list[str] = []

    for word in code.split("   "):
        decoded_word: list[str] = []

        for letter in word.split(" "):
            decoded_word.append(MORSE_CODE[letter])

        decoded_words.append("".join(decoded_word))

    return " ".join(decoded_words)


print(decode_morse("--.."))
print(decode_morse("... --- ..."))
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))
