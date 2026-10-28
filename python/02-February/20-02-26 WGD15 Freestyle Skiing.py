"""
2026 Winter Games Day 15: Freestyle Skiing
Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid
second words.

The two words will be separated by a single space.

Valid first words:
"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"

Valid second words:
"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"

1. is_valid_trick("Polar Vortex") should return True.
2. is_valid_trick("Solar Icequake") should return True.
3. is_valid_trick("Thunder Blizzard") should return True.
4. is_valid_trick("Phantom Frostbite") should return True.
5. is_valid_trick("Ghost Avalanche") should return True.
6. is_valid_trick("Snowstorm Shadow") should return False.
7. is_valid_trick("Solar Sky") should return False.
"""

def is_valid_trick(trick_name: str) -> bool:
    valid_first_words: set[str] = {"Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"}
    valid_second_words: set[str] = {"Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard",
                                     "Shadow"}
    trick_name_list: list[str] = trick_name.split()

    if trick_name_list[0] in valid_first_words and trick_name_list[1] in valid_second_words:
        return True

    return False


print(is_valid_trick("Polar Vortex"))
print(is_valid_trick("Solar Icequake"))
print(is_valid_trick("Thunder Blizzard"))
print(is_valid_trick("Phantom Frostbite"))
print(is_valid_trick("Ghost Avalanche"))
print(is_valid_trick("Snowstorm Shadow"))
print(is_valid_trick("Solar Sky"))
