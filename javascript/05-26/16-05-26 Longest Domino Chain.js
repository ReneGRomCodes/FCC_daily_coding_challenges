/*
Longest Domino Chain
Given a 2D array representing a set of dominoes, return the longest valid chain.

- Each domino is a pair of numbers from 0–6, e.g. [3, 2].
- A chain is valid when the second number of each domino matches the first number of the next.
- The first number of the first domino and the second number of the last one don't need to match anything.
- Any domino can be flipped, so [3, 2] can be played as [2, 3].
- There is always exactly one longest valid chain.

For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]].

1. get_longest_chain([[1, 2], [4, 5], [2, 3]]) should return [[1, 2], [2, 3]].
2. get_longest_chain([[2, 1], [4, 3], [5, 3]]) should return [[4, 3], [3, 5]].
3. get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]) should return [[1, 2], [2, 3], [3, 4], [4, 0]].
4. get_longest_chain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]])
    should return [[4, 1], [1, 1], [1, 6], [6, 6], [6, 5]].
5. get_longest_chain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]])
    should return [[3, 3], [3, 0], [0, 4], [4, 4], [4, 5], [5, 5], [5, 6]].
 */

function getLongestChain(dominoes) {
    let bestChain = [];

    function dfs(currentDomino, currentChain) {
        if (currentChain.length > bestChain.length) {
            bestChain = [...currentChain];
        }

        const trailingNum = currentDomino[1];

        for (let i = 0; i < dominoes.length; i++) {
            const nextDomino = dominoes[i];

            if (nextDomino === null) continue;

            if (nextDomino[0] === trailingNum) {
                dominoes[i] = null;
                currentChain.push(nextDomino);
                dfs(nextDomino, currentChain);
                currentChain.pop();
                dominoes[i] = nextDomino;
            } else if (nextDomino[1] === trailingNum) {
                const flipped = [nextDomino[1], nextDomino[0]];
                dominoes[i] = null;
                currentChain.push(flipped);
                dfs(flipped, currentChain);
                currentChain.pop();
                dominoes[i] = nextDomino;
            }
        }
    }

    for (let i = 0; i < dominoes.length; i++) {
        const startDomino = dominoes[i];
        dominoes[i] = null;
        dfs(startDomino, [startDomino]);
        dfs([startDomino[1], startDomino[0]], [[startDomino[1], startDomino[0]]]);
        dominoes[i] = startDomino;
    }
    return bestChain;
}


console.log(getLongestChain([[1, 2], [4, 5], [2, 3]]));
console.log(getLongestChain([[2, 1], [4, 3], [5, 3]]));
console.log(getLongestChain([[1, 2], [3, 4], [2, 3], [4, 0]]));
console.log(getLongestChain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]]));
console.log(getLongestChain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]]));
