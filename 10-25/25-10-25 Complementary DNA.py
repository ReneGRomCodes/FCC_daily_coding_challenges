"""
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".

1. complementary_dna("ACGT") should return "TGCA".
2. complementary_dna("ATGCGTACGTTAGC") should return "TACGCATGCAATCG".
3. complementary_dna("GGCTTACGATCGAAG") should return "CCGAATGCTAGCTTC".
4. complementary_dna("GATCTAGCTAGGCTAGCTAG") should return "CTAGATCGATCCGATCGATC".
"""

def complementary_dna(strand: str) -> str:
    dna_dict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    compl_dna: str = ""

    for char in strand:
        compl_dna += dna_dict[char]

    return compl_dna


print(complementary_dna("ACGT"))
print(complementary_dna("ATGCGTACGTTAGC"))
print(complementary_dna("GGCTTACGATCGAAG"))
print(complementary_dna("GATCTAGCTAGGCTAGCTAG"))
