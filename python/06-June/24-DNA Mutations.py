"""
DNA Mutations
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).

- DNA strands are strings made up of the characters "A", "T", "C", and "G"
- Return the indexes in ascending order
- If there are no mutations, return an empty array

1. detect_mutations("ATCG", "ATGG") should return [2].
2. detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC") should return [4, 9, 11].
3. detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG") should return [].
4. detect_mutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG")
    should return [15, 16, 17, 18].
5. detect_mutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT")
    should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27, 28].
"""

def detect_mutations(strand1: str, strand2: str) -> list[int]:
    mutations: list[int] = []

    for i, char in enumerate(strand1):
        if char != strand2[i]:
            mutations.append(i)

    return mutations


print(detect_mutations("ATCG", "ATGG"))
print(detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"))
print(detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"))
print(detect_mutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"))
print(detect_mutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT"))
