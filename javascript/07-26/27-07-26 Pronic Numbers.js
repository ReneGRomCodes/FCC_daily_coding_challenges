/*
Pronic Number
Given a number, determine whether it is a pronic number.

A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.

1. is_pronic(6) should return True.
2. is_pronic(15) should return False.
3. is_pronic(12) should return True.
4. is_pronic(132) should return True.
5. is_pronic(80) should return False.
6. is_pronic(0) should return True.
 */

function isPronic(n) {
    if (n === 0) { return true }

    for (let i = 0; i <= n; i++) {
        if (i * (i + 1) === n) {
            return true;
        } else if (i * (i + 1) > n) {
            return false;
        }
    }
}


console.log(isPronic(6));
console.log(isPronic(15));
console.log(isPronic(12));
console.log(isPronic(132));
console.log(isPronic(80));
console.log(isPronic(0));
