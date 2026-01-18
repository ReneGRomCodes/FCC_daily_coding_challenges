"""
Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled
accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given.

1. scale_recipe(["2 C Flour", "1.5 T Sugar"], 2) should return ["4 C Flour", "3 T Sugar"].
2. scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5) should return ["6 T Flour", "1.5 C Milk", "3 T Oil"].
3. scale_recipe(["3 C Milk", "2 C Oats"], 0.5) should return ["1.5 C Milk", "1 C Oats"].
4. scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar",
   "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5)
        should return ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar",
        "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"].
"""

def scale_recipe(ingredients: list[str], scale: int | float) -> list[str]:
    ingredients_array: list[list[str]] = [ingredient.split() for ingredient in ingredients]
    scaled_ingredients: list[str] = []

    for arr in ingredients_array:
        new_quantity: float = float(arr[0]) * scale

        if new_quantity % 1 == 0:
            arr[0]: str = str(int(new_quantity))
        else:
            arr[0]: str = str(new_quantity)

        scaled_ingredients.append(" ".join(arr))

    return scaled_ingredients


print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2))
print(scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5))
print(scale_recipe(["3 C Milk", "2 C Oats"], 0.5))
print(scale_recipe(
    ["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar",
     "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5)
)
