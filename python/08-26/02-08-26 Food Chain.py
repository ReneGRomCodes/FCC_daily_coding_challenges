"""
Food Chain
Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.

- The apex predator is the animal that is never prey to another animal.
- Return the chain as an array of strings.

1. get_food_chain([["cat", "mouse"]]) should return ["cat", "mouse"].
2. get_food_chain([["wolf", "deer"], ["deer", "grass"]]) should return ["wolf", "deer", "grass"].
3. get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]) should return ["hawk", "snake", "frog", "fly"].
4. get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]) should return ["eagle", "fox", "rabbit", "grass"].
5. get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]])
    should return ["orca", "seal", "salmon", "herring", "shrimp", "plankton"].
"""

def find_apex_predator(pairs: list[list[str]]) -> list[str]:
    """
    Create and return food chain list with apex predator as first entry.
    ARGS:
        pairs: Array of predator-prey pairs.
    RETURNS:
        food_chain: list including apex predator from 'pairs'.
    """
    animals_set: set[str] = set([animals for pair in pairs for animals in pair])
    prey_predator: dict[str, str] = {}
    food_chain: list[str] = []

    for pair in pairs:
        prey_predator[pair[1]] = pair[0]

    for animal in animals_set:
        if animal not in prey_predator:
            food_chain.append(animal)
            break

    return food_chain


def get_food_chain(pairs: list[list[str]]) -> list[str]:
    predator_prey: dict[str, str] = {}
    food_chain: list[str] = find_apex_predator(pairs)  # Get starting list that includes the apex predator.

    for pair in pairs:
        predator_prey[pair[0]] = pair[1]

    while len(predator_prey) > 0:
        current_animal: str = food_chain[-1]

        if current_animal in predator_prey:
            food_chain.append(predator_prey[current_animal])
            del predator_prey[current_animal]

    return food_chain


print(get_food_chain([["cat", "mouse"]]))
print(get_food_chain([["wolf", "deer"], ["deer", "grass"]]))
print(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]))
print(get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]))
print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]))
