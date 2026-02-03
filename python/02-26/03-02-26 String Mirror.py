"""
String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end
of it.

1. mirror("freeCodeCamp") should return "freeCodeCamppmaCedoCeerf".
2. mirror("RaceCar") should return "RaceCarraCecaR".
3. mirror("helloworld") should return "helloworlddlrowolleh".
4. mirror("The quick brown fox...") should return "The quick brown fox......xof nworb kciuq ehT".
"""

def mirror(s: str) -> str:
    return s + s[::-1]


print(mirror("freeCodeCamp"))
print(mirror("RaceCar"))
print(mirror("helloworld"))
print(mirror("The quick brown fox..."))
