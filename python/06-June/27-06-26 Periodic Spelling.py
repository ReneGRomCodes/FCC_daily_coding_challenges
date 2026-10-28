"""
Periodic Spelling
Given a word, determine if it can be spelled using element symbols from the periodic table.

- Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".

Here's a full list of the element symbols:
["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe",
"Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
"Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W",
"Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf",
"Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];

Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or,
an empty array if it can't be spelled.

1. get_periodic_spelling("neon") should return ["Ne", "O", "N"].
2. get_periodic_spelling("rational") should return ["Ra", "Ti", "O", "N", "Al"].
3. get_periodic_spelling("yarn") should return ["Y", "Ar", "N"].
4. get_periodic_spelling("carbon") should return ["C", "Ar", "B", "O", "N"] or ["Ca", "Rb", "O", "N"].
5. get_periodic_spelling("noisy") should return ["N", "O", "I", "S", "Y"] or ["No", "I", "S", "Y"].
6. get_periodic_spelling("bicycles") should return ["B", "I", "C", "Y", "Cl", "Es"] or ["Bi", "C", "Y", "Cl", "Es"].
7. get_periodic_spelling("optics") should return ["O", "P", "Ti", "C", "S"], ["O", "P", "Ti", "Cs"], ["O", "Pt", "I", "C", "S"], or ["O", "Pt", "I", "Cs"].
8. get_periodic_spelling("value") should return [].
"""

ELEMENTS = {
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc",
    "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
    "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm",
    "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl",
    "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
    "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
}


def backtrack(word: str, position: int) -> list[str] | None:
    """Recursively find a valid element-symbol spelling from the given position.

    ARGS:
        word: str to check for element combinations.
        position: Index of the character from which to continue checking the word.
    RETURNS:
        List of element symbols if the remaining substring can be spelled, or None if no valid spelling is possible."""
    if position == len(word):
        return []

    for length in (2, 1):
        symbol: str = word[position:position + length]
        match: str | None = next((element for element in ELEMENTS if element.lower() == symbol), None)

        if match is None:
            continue

        result: list[str] | None = backtrack(word, position + length)

        if result is not None:
            return [match] + result

    return None


def get_periodic_spelling(word: str) -> list[str]:
    return backtrack(word.lower(), 0) or []


print(get_periodic_spelling("neon"))
print(get_periodic_spelling("rational"))
print(get_periodic_spelling("yarn"))
print(get_periodic_spelling("carbon"))
print(get_periodic_spelling("noisy"))
print(get_periodic_spelling("bicycles"))
print(get_periodic_spelling("optics"))
print(get_periodic_spelling("value"))
