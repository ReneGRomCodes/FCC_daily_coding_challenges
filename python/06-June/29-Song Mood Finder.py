"""
Song Mood Finder

Given a genre string and a BPM number for a song, determine the mood using the following table:
Mood	Genre	        BPM Range
"focus"	"classical"	    60–109
"focus"	"electronic"	60–89
"happy"	"pop"	        60–180
"happy"	"classical"	    110–180
"happy"	"rock"	        60–129
"happy"	"electronic"	90–134
"hype"	"rock"	        130–180
"hype"	"electronic"	135–180

1. get_mood("rock", 111) should return "happy".
2. get_mood("electronic", 74) should return "focus".
3. get_mood("classical", 180) should return "happy".
4. get_mood("rock", 155) should return "hype".
5. get_mood("electronic", 90) should return "happy".
6. get_mood("classical", 67) should return "focus".
7. get_mood("pop", 100) should return "happy".
8. get_mood("electronic", 135) should return "hype".
"""

def get_mood(genre: str, bpm: int) -> str | None:
    moods: dict[str, dict[str, tuple[int, int]]] = {
        "classical": {
            "focus": (60, 109),
            "happy": (110, 180),
        },
        "electronic": {
            "focus": (60, 89),
            "happy": (90, 134),
            "hype": (135, 180),
        },
        "pop": {
            "happy": (60, 180),
        },
        "rock": {
            "happy": (60, 129),
            "hype": (130, 180),
        },
    }

    for k, v in moods[genre].items():
        if v[0] <= bpm <= v[1]:
            return k

    return None


print(get_mood("rock", 111))
print(get_mood("electronic", 74))
print(get_mood("classical", 180))
print(get_mood("rock", 155))
print(get_mood("electronic", 90))
print(get_mood("classical", 67))
print(get_mood("pop", 100))
print(get_mood("electronic", 135))
