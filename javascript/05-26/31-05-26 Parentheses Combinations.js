/*
Parentheses Combinations
Given an integer, n, return the number of valid combinations of n pairs of parentheses.

- A valid combination is a string where every opening parentheses has a corresponding closing parentheses, and no closing
  parentheses appears before its matching opening parentheses.

For example, given 2, there are 2 valid combinations:
(())
()()

1. get_combinations(2) should return 2.
2. get_combinations(3) should return 5.
3. get_combinations(5) should return 42.
4. get_combinations(8) should return 1430.
5. get_combinations(13) should return 742900.
 */

function getCombinations(n) {
    let count = 1;

    for (let i = 0; i < n; i++) {
        count = Math.floor((count * (2 * (2 * i + 1))) / (i + 2));
    }

    return count;
}


console.log(getCombinations(2));
console.log(getCombinations(3));
console.log(getCombinations(5));
console.log(getCombinations(8));
console.log(getCombinations(13));
