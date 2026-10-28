"""
Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the
given allergens.

- Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the
  allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
- Allergens to avoid will be an array of strings.

Return safe meal names in the same order given. If no meal is safe, return an empty array.

1. get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]) should return ["salad"].
2. get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]],
    ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]) should return ["fried rice", "chicken parmesan"].
3. get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []],
    ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"])
        should return ["oatmeal", "granola", "toast"].
4. get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []],
    ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"])
        should return ["granola", "yogurt", "eggs"].
"""

def get_allergen_friendly_meals(meals: list, allergens: list) -> list:
    allergen_free_list: list = []

    for meal in meals:
        has_allergens = False

        for allergen in meal[1]:
            if allergen in allergens:
                has_allergens = True
                continue

        if not has_allergens:
            allergen_free_list.append(meal[0])

    return allergen_free_list


print(get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]],
                                  ["milk"]))
print(get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]],
                                  ["soy", "fish"]))
print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]],
                                  ["eggs", "milk"]))
print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]],
                                  ["wheat", "nuts"]))
