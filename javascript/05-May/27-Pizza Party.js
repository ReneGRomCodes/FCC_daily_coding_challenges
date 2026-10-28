/*
Pizza Party
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

- Divide each person's hours worked by 3 to get their slice count.
- You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
- Each person gets a minimum of two slices.
- Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.

1. getPizzasToOrder([8, 8, 8]) should return 2.
2. getPizzasToOrder([10, 9, 8, 2, 2, 6, 10]) should return 3.
3. getPizzasToOrder([1, 2, 3, 4, 5]) should return 2.
4. getPizzasToOrder([8, 8, 8, 8, 8, 8, 8, 8]) should return 3.
5. getPizzasToOrder([9, 9, 6]) should return 1.
6. getPizzasToOrder([10, 12, 16, 9, 8, 11, 15, 8, 0]) should return 5.
 */

function getPizzasToOrder(hoursWorked) {
    const slices = [];

    for (const worked of hoursWorked) {
        const slicePp = Math.ceil(worked / 3);
        slicePp < 2 ? slices.push(2) : slices.push(slicePp);
    }

    return Math.ceil(slices.reduce((a, b) => a + b, 0) / 8);
}


console.log(getPizzasToOrder([8, 8, 8]));
console.log(getPizzasToOrder([10, 9, 8, 2, 2, 6, 10]));
console.log(getPizzasToOrder([1, 2, 3, 4, 5]));
console.log(getPizzasToOrder([8, 8, 8, 8, 8, 8, 8, 8]));
console.log(getPizzasToOrder([9, 9, 6]));
console.log(getPizzasToOrder([10, 12, 16, 9, 8, 11, 15, 8, 0]));
