/*
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
 */

function getFoodChain(pairs) {
    const preyPredator = new Map();
    const predatorPrey = new Map();
    const animals = new Set();
    const foodChain = [];

    for (const [predator, prey] of pairs) {
        preyPredator.set(prey, predator);
        predatorPrey.set(predator, prey);

        animals.add(predator);
        animals.add(prey);
    }

    for (const animal of animals) {
        if (!preyPredator.has(animal)) {
            foodChain.push(animal);
            break;
        }
    }

    while (predatorPrey.size > 0) {
        const currentAnimal = foodChain.at(-1);

        if (predatorPrey.has(currentAnimal)) {
            const prey = predatorPrey.get(currentAnimal);

            foodChain.push(prey);
            predatorPrey.delete(currentAnimal);
        }
    }

    return foodChain;
}


console.log(getFoodChain([["cat", "mouse"]]));
console.log(getFoodChain([["wolf", "deer"], ["deer", "grass"]]));
console.log(getFoodChain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]));
console.log(getFoodChain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]));
console.log(getFoodChain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]));
