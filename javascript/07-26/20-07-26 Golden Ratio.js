/*
Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.

- Use a golden ratio of 1.618
- Allow a tolerance of 0.01

1. is_golden_ratio(21, 34) should return True.
2. is_golden_ratio(15, 20) should return False.
3. is_golden_ratio(8, 13) should return True.
4. is_golden_ratio(10, 16) should return False.
5. is_golden_ratio(1618, 1000) should return True.
6. is_golden_ratio(88, 55) should return False.
 */

function isGoldenRatio(a, b) {
    const goldenRatio = 1.618;
    const tolerance = 0.01;
    const ratio = Math.max(a, b) / Math.min(a, b);

    return Math.abs(goldenRatio - ratio) <= tolerance;
}


console.log(isGoldenRatio(21, 34));
console.log(isGoldenRatio(15, 20));
console.log(isGoldenRatio(8, 13));
console.log(isGoldenRatio(10, 16));
console.log(isGoldenRatio(1618, 1000));
console.log(isGoldenRatio(88, 55));
