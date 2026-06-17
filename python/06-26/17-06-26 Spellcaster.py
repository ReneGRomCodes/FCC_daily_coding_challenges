"""
Spellcaster
Given a string of spell codes you are casting, calculate the total score.

Each character in the string represents a spell:

Code	Spell	    Category	    Base Score
"f"	    Fire	    Destruction	    3
"l"	    Lightning	Destruction	    3
"i"	    Ice	        Control	        2
"w"	    Wind	    Control	        2
"h"	    Heal	    Restoration	    1
"s"	    Shield	    Restoration	    1

A combo multiplier is applied based on how many spells in a row have been cast from different categories:

- The first spell always scores at base value.
- Each consecutive spell from a different category than the previous increases the multiplier by 1.
- Casting a spell from the same category as the previous resets the multiplier back to 1.
- The score for each spell is its base score multiplied by the current multiplier.

Return the total score from the sequence of spells.

1. cast("fihwl") should return 33.
2. cast("lwswfi") should return 45.
3. cast("wislhfl") should return 37.
4. cast("sihwlih") should return 50.
5. cast("wishlfihwslwifihl") should return 101.
"""

def cast(spells: str) -> int:
    spells_dict: dict[str, tuple[str, int]] = {
        "f": ("Destruction", 3),
        "l": ("Destruction", 3),
        "i": ("Control", 2),
        "w": ("Control", 2),
        "h": ("Restoration", 1),
        "s": ("Restoration", 1),
    }
    current_cat: str = spells_dict[spells[0]][0]
    multiplier: int = 1
    total_score: int = 0

    for spell in spells:
        spell_cat, spell_score = spells_dict[spell][0], spells_dict[spell][1]

        if spell_cat != current_cat:
            multiplier += 1
            current_cat = spell_cat
        else:
            multiplier = 1

        total_score += spell_score * multiplier

    return total_score


print(cast("fihwl"))
print(cast("lwswfi"))
print(cast("wislhfl"))
print(cast("sihwlih"))
print(cast("wishlfihwslwifihl"))
