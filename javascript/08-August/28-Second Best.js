/*
Second Best
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.

1. get_laptop_cost([1500, 2000, 1800, 1400], 1900) should return 1800
2. get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) should return 1800
3. get_laptop_cost([2099, 1599, 1899, 1499], 2200) should return 1899
4. get_laptop_cost([2099, 1599, 1899, 1499], 1000) should return 0
5. get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) should return 1400
 */

function getLaptopCost(laptops, budget) {
    laptops.splice(laptops.indexOf(Math.max(...laptops)), 1);  // Remove most expensive Laptop first.
    let foundLaptop = false;

    while (!foundLaptop) {
        if (laptops.length !== 0) {
            if (Math.max(...laptops) > budget) {
                laptops.splice(laptops.indexOf(Math.max(...laptops)), 1);
            } else if (Math.max(...laptops) <= budget) {
                foundLaptop = Math.max(...laptops);
            }

        } else {
            return 0;
        }
    }

    return foundLaptop;
}


console.log(getLaptopCost([1500, 2000, 1800, 1400], 1900));
console.log(getLaptopCost([1500, 2000, 2000, 1800, 1400], 1900));
console.log(getLaptopCost([2099, 1599, 1899, 1499], 2200));
console.log(getLaptopCost([2099, 1599, 1899, 1499], 1000));
console.log(getLaptopCost([1200, 1500, 1600, 1800, 1400, 2000], 1450));
