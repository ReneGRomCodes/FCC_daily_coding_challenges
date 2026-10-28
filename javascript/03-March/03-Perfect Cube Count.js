/*
Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube
because 3 * 3 * 3 = 27.

1. count_perfect_cubes(3, 30) should return 2.
2. count_perfect_cubes(1, 30) should return 3.
3. count_perfect_cubes(30, 0) should return 4.
4. count_perfect_cubes(-64, 64) should return 9.
5. count_perfect_cubes(9214, -8127) should return 41.
 */

// Not the most optimal solution, but I wanted to fiddle around with the floating point problem in the for-loop a bit.
function countPerfectCubes(a, b) {
    const cubeRange = [Math.min(a, b), Math.max(a, b)];
    let counter = 0;

    for (let i = cubeRange[0]; i <= cubeRange[1]; i++) {
        if (Math.round(Math.cbrt(i)) ** 3 === i) {
            counter++;
        }
    }

    return counter;
}


// Optimized solution.
function countPerfectCubesOptimized(a, b) {
    const lower = Math.min(a, b);
    const upper = Math.max(a, b);

    const start = Math.ceil(Math.cbrt(lower));
    const end = Math.floor(Math.cbrt(upper));

    return Math.max(0, end - start + 1);
}


console.log(countPerfectCubes(3, 30));
console.log(countPerfectCubes(1, 30));
console.log(countPerfectCubes(30, 0));
console.log(countPerfectCubes(-64, 64));
console.log(countPerfectCubes(9214, -8127));
