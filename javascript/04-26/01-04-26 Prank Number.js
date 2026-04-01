/*
Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't
follow the pattern fixed.

The pattern will be one of:
- The numbers increase from one to the next by a fixed amount (addition).
- The numbers decrease from one to the next by a fixed amount (subtraction).

For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

1. fix_prank_number([2, 4, 7, 8, 10]) should return [2, 4, 6, 8, 10].
2. fix_prank_number([10, 10, 8, 7, 6]) should return [10, 9, 8, 7, 6].
3. fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]) should return [12, 24, 36, 48, 60, 72, 84, 96].
4. fix_prank_number([4, 1, -2, -5, -8, -5]) should return [4, 1, -2, -5, -8, -11].
5. fix_prank_number([0, 100, 200, 300, 150, 500]) should return [0, 100, 200, 300, 400, 500].
6. fix_prank_number([400, 425, 400, 375, 350, 325, 300]) should return [450, 425, 400, 375, 350, 325, 300].
7. fix_prank_number([-5, 5, 10, 15, 20]) should return [0, 5, 10, 15, 20].
 */

function fixPrankNumber(arr) {
    // Step 1: compute differences.
    const steps = [];
    for (let i = 0; i < arr.length - 1; i++) {
        steps.push(arr[i + 1] - arr[i]);
    }

    // Step 2: find most common step.
    const stepCount = {};
    for (const step of steps) {
        stepCount[step] = (stepCount[step] || 0) + 1;
    }

    let correctStep = steps[0];
    for (const step in stepCount) {
        if (stepCount[step] > stepCount[correctStep]) {
            correctStep = Number(step);
        }
    }

    // Helper to build candidate sequence.
    function buildCandidate(start) {
        const result = [];
        for (let i = 0; i < arr.length; i++) {
            result.push(start + i * correctStep);
        }
        return result;
    }

    // Step 3: try candidate sequence using first element from 'arr'.
    let candidateSequence = buildCandidate(arr[0]);

    // Step 4: count mismatches.
    let mismatches = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== candidateSequence[i]) {
            mismatches++;
        }
    }

    // Step 5: decide.
    if (mismatches <= 1) {
        return candidateSequence;
    } else {
        // First element must be wrong -> recompute sequence from second element.
        const start = arr[1] - correctStep;
        return buildCandidate(start);
    }
}


console.log(fixPrankNumber([2, 4, 7, 8, 10]));
console.log(fixPrankNumber([10, 10, 8, 7, 6]));
console.log(fixPrankNumber([12, 24, 36, 48, 61, 72, 84, 96]));
console.log(fixPrankNumber([4, 1, -2, -5, -8, -5]));
console.log(fixPrankNumber([0, 100, 200, 300, 150, 500]));
console.log(fixPrankNumber([400, 425, 400, 375, 350, 325, 300]));
console.log(fixPrankNumber([-5, 5, 10, 15, 20]));
