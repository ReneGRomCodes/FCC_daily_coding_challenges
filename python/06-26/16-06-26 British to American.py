"""
British to American
Given a sentence, convert any British English spellings to their American English equivalents using the following lookup
table and return the updated sentence:

British	    American
"colour"	"color"
"flavour"	"flavor"
"honour"	"honor"
"neighbour"	"neighbor"
"labour"	"labor"
"humour"	"humor"
"centre"	"center"
"fibre"	    "fiber"
"defence"	"defense"
"offence"	"offense"
"organise"	"organize"
"recognise"	"recognize"
"analyse"	"analyze"

- Replacements should be case-insensitive. For example, "Colour" should become "Color".
- The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For
  example, "colouring" should become "coloring", and "disorganised" should become "disorganized".

1. british_to_american("I love the colour blue.") should return "I love the color blue."
2. british_to_american("The fibre optic cable is new.") should return "The fiber optic cable is new."
3. british_to_american("It's an honour to meet someone with such humour.") should return "It's an honor to meet someone with such humor."
4. british_to_american("The unrecognised artist analysed his colour palette at the centre.")
    should return "The unrecognized artist analyzed his color palette at the center."
5. british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful.")
    should return The offense analyzed, with organisation, the defense center and recognized that the neighboring laboror was humorous, flavorful, and colorful.
"""


def british_to_american(sentence: str) -> str:
    gb_to_us_lookup: dict[str, str] = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze",
    }

    for gb, us in gb_to_us_lookup.items():
        sentence = sentence.replace(gb, us)
        sentence = sentence.replace(gb.capitalize(), us.capitalize())

    return sentence


print(british_to_american("I love the colour blue."))
print(british_to_american("The fibre optic cable is new."))
print(british_to_american("It's an honour to meet someone with such humour."))
print(british_to_american("The unrecognised artist analysed his colour palette at the centre."))
print(british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."))
