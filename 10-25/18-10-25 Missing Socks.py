"""
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
"""

def sock_pairs(pairs: int, cycles: int) -> int:
    socks = pairs * 2

    lost_socks = -(cycles // 2)
    found_socks = cycles // 3
    worn_out_socks = -(cycles // 5)
    bought_socks = cycles // 10 * 2

    pairs = int((socks + lost_socks + found_socks + worn_out_socks + bought_socks) / 2)

    return pairs


print(sock_pairs(2, 5))
print(sock_pairs(1, 2))
print(sock_pairs(5, 11))
print(sock_pairs(6, 25))
print(sock_pairs(1, 8))
