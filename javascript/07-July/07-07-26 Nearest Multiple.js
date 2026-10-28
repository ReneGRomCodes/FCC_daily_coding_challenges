/*
Nearest Multiple
Given two integers, round the first to the nearest multiple of the second.

1. round_to_nearest_multiple(5, 3) should return 6.
2. round_to_nearest_multiple(17, 4) should return 16.
3. round_to_nearest_multiple(43, 5) should return 45.
4. round_to_nearest_multiple(38, 11) should return 33.
5. round_to_nearest_multiple(93, 12) should return 96.
 */

function roundToNearestMultiple(num, multiple) {
    let multiplicator = 2;
    let lowerProduct = multiple;
    let higherProduct = multiple * multiplicator;

    while (num > higherProduct) {
        multiplicator += 1;
        lowerProduct = multiple * multiplicator;
        higherProduct = multiple * (multiplicator + 1);
    }

    return Math.abs(num - lowerProduct) < Math.abs(num - higherProduct) ? lowerProduct : higherProduct;
}


console.log(roundToNearestMultiple(5, 3));
console.log(roundToNearestMultiple(17, 4));
console.log(roundToNearestMultiple(43, 5));
console.log(roundToNearestMultiple(38, 11));
console.log(roundToNearestMultiple(93, 12));
