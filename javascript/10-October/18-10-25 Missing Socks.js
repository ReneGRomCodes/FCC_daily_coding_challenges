/*
Missing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many
wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following
constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new
pair of socks.

Return the number of complete pairs of socks.
1. sock_pairs(2, 5) should return 1.
2. sock_pairs(1, 2) should return 0.
3. sock_pairs(5, 11) should return 4.
4. sock_pairs(6, 25) should return 3.
5. sock_pairs(1, 8) should return 0.
 */

function sockPairs(pairs, cycles) {
    const socks = pairs * 2;
    const lostSocks = -(Math.floor(cycles / 2));
    const foundSocks = Math.floor(cycles / 3);
    const wornOutSocks = -(Math.floor(cycles / 5));
    const boughtSocks = Math.floor(cycles / 10) * 2;
    const totalSocks = Math.max(0, socks + lostSocks + foundSocks + wornOutSocks + boughtSocks);

    return Math.floor(totalSocks / 2);
}


console.log(sockPairs(2, 5));
console.log(sockPairs(1, 2));
console.log(sockPairs(5, 11));
console.log(sockPairs(6, 25));
console.log(sockPairs(1, 8));
