"""
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
"""


def get_longest_chain(dominoes: list[list[int]]) -> list[list[int]]:
    best_chain: list[list[int]] = []

    def dfs(current_domino, remaining_dominoes, current_chain):
        nonlocal best_chain

        if len(current_chain) > len(best_chain):
            best_chain = list(current_chain)

        trailing_num: list[int] = current_domino[1]

        for i, next_domino in enumerate(remaining_dominoes):
            if next_domino[0] == trailing_num:
                next_pool: list[int] = remaining_dominoes[:i] + remaining_dominoes[i + 1:]
                dfs(next_domino, next_pool, current_chain + [next_domino])

            elif next_domino[1] == trailing_num:
                flipped: list[int] = [next_domino[1], next_domino[0]]
                next_pool = remaining_dominoes[:i] + remaining_dominoes[i + 1:]
                dfs(flipped, next_pool, current_chain + [flipped])

    for i, start_domino in enumerate(dominoes):
        pool_without_start: list[list[int]] = dominoes[:i] + dominoes[i + 1:]
        dfs(start_domino, pool_without_start, [start_domino])
        flipped_start: list[int] = [start_domino[1], start_domino[0]]
        dfs(flipped_start, pool_without_start, [flipped_start])

    return best_chain


print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))
print(get_longest_chain([[2, 1], [4, 3], [5, 3]]))
print(get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]))
print(get_longest_chain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]]))
print(get_longest_chain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]]))
