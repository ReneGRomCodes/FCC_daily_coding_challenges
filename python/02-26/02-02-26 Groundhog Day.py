"""
Groundhog Day
Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of
winter.".
If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
If the value is anything else (the groundhog did not show up), return "No prediction this year.".

1. groundhog_day_prediction(True) should return "Looks like we'll have six more weeks of winter.".
2. groundhog_day_prediction(False) should return "It's going to be an early spring.".
3. groundhog_day_prediction(None) should return "No prediction this year.".
4. groundhog_day_prediction(" ") should return "No prediction this year.".
5. groundhog_day_prediction("True") should return "No prediction this year.".
"""

def groundhog_day_prediction(appearance: bool | None | str) -> str:
    if appearance is True:
        return "Looks like we'll have six more weeks of winter."
    elif appearance is False:
        return "It's going to be an early spring."
    else:
        return "No prediction this year."


print(groundhog_day_prediction(True))
print(groundhog_day_prediction(False))
print(groundhog_day_prediction(None))
print(groundhog_day_prediction(" "))
print(groundhog_day_prediction("True"))
