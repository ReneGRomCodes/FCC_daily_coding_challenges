/*
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
 */

function complementaryDNA(strand) {

    return strand;
}


console.log(complementaryDNA("ACGT"));
console.log(complementaryDNA("ATGCGTACGTTAGC"));
console.log(complementaryDNA("GGCTTACGATCGAAG"));
console.log(complementaryDNA("GATCTAGCTAGGCTAGCTAG"));
