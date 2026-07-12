/*
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
 */

function horoscopeMatch(sign1, sign2) {
    const signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn",
        "Aquarius", "Pisces"];
    const compatibility = {0: "100%", 1: "40%", 2: "80%", 3: "30%", 4: "90%", 5: "20%", 6: "50%"};
    const [sign1_index, sign2_index] = [signs.indexOf(sign1), signs.indexOf(sign2)];
    const distance = Math.max(sign1_index, sign2_index) - Math.min(sign1_index, sign2_index);

    return compatibility[Math.min(distance, signs.length - distance)];
}


console.log(horoscopeMatch("Libra", "Sagittarius"));
console.log(horoscopeMatch("Gemini", "Scorpio"));
console.log(horoscopeMatch("Pisces", "Aries"));
console.log(horoscopeMatch("Capricorn", "Cancer"));
console.log(horoscopeMatch("Aquarius", "Aquarius"));
console.log(horoscopeMatch("Virgo", "Taurus"));
console.log(horoscopeMatch("Leo", "Scorpio"));
