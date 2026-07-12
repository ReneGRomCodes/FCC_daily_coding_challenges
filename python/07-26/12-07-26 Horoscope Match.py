"""
Horoscope Match
Given two star sign strings, return their compatibility percentage.

The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
"Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries" after "Pisces".

Find the shortest distance between the two signs and return the compatibility:
Distance	Compatibility
0	        "100%"
1	        "40%"
2	        "80%"
3	        "30%"
4	        "90%"
5	        "20%"
6	        "50%"

1. horoscope_match("Libra", "Sagittarius") should return "80%".
2. horoscope_match("Gemini", "Scorpio") should return "20%".
3. horoscope_match("Pisces", "Aries") should return "40%".
4. horoscope_match("Capricorn", "Cancer") should return "50%".
5. horoscope_match("Aquarius", "Aquarius") should return "100%".
6. horoscope_match("Virgo", "Taurus") should return "90%".
7. horoscope_match("Leo", "Scorpio") should return "30%".
"""

def horoscope_match(sign1: str, sign2: str) -> str:
    signs: tuple[str, ...] = ("Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius",
                              "Capricorn", "Aquarius", "Pisces")
    compatibility: dict[int, str] = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%",
    }
    sign1_index, sign2_index = signs.index(sign1), signs.index(sign2)
    distance: int = max(sign1_index, sign2_index) - min(sign1_index, sign2_index)

    return compatibility[min(distance, len(signs) - distance)]


print(horoscope_match("Libra", "Sagittarius"))
print(horoscope_match("Gemini", "Scorpio"))
print(horoscope_match("Pisces", "Aries"))
print(horoscope_match("Capricorn", "Cancer"))
print(horoscope_match("Aquarius", "Aquarius"))
print(horoscope_match("Virgo", "Taurus"))
print(horoscope_match("Leo", "Scorpio"))
