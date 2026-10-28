/*
Digit Rotation Escape
Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

- Check rotation 0 (the given number) first.
- Given numbers won't contain any zeros.
- Return the first rotation number if one is found, or "none" if not.

1. get_rotation(123) should return 0.
2. get_rotation(13579) should return 3.
3. get_rotation(24681) should return "none".
4. get_rotation(84138789345) should return 6.
 */

function getRotation(n) {
    let nString = n.toString();
    const length = nString.length;

    for (let i = 0; i < length; i++) {
        if (nString % length === 0) {
            return i;
        } else {
            nString = nString.slice(1) + nString.slice(0, 1);
        }
    }

    return "none";
}


console.log(getRotation(123));
console.log(getRotation(13579));
console.log(getRotation(24681));
console.log(getRotation(84138789345));
