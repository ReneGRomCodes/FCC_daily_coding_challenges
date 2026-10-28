"""
Playing Card Values
Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

An Ace ("A") has a value of 1.
Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:

Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:

Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts,
and "QC" is the Queen of Clubs.

1. card_values(["3H", "4D", "5S"]) should return [3, 4, 5].
2. card_values(["AS", "10S", "10H", "6D", "7D"]) should return [1, 10, 10, 6, 7].
3. card_values(["8D", "QS", "2H", "JC", "9C"]) should return [8, 10, 2, 10, 9].
4. card_values(["AS", "KS"]) should return [1, 10].
5. card_values(["10H", "JH", "QH", "KH", "AH"]) should return [10, 10, 10, 10, 1].
"""

def card_values(cards: list[str]) -> list[int]:
    unnumbered_values: dict[str, int] = {
        "A": 1,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    result: list[int] = []

    for card in cards:
        value = card[:-1]
        if value in unnumbered_values:
            result.append(unnumbered_values[value])
        else:
            result.append(int(value))

    return result


print(card_values(["3H", "4D", "5S"]))
print(card_values(["AS", "10S", "10H", "6D", "7D"]))
print(card_values(["8D", "QS", "2H", "JC", "9C"]))
print(card_values(["AS", "KS"]))
print(card_values(["10H", "JH", "QH", "KH", "AH"]))
