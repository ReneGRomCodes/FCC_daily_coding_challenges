/*
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
 */

const ELEMENTS = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc",
    "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
    "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm",
    "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl",
    "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
    "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
];


// Recursively find a valid element-symbol spelling from the given position.
function backtrack(word, position) {
    if (position === word.length) {
        return [];
    }

    for (const length of [2, 1]) {
        const symbol = word.slice(position, position + length);

        const match = ELEMENTS.find(element => element.toLowerCase() === symbol);

        if (match === undefined) {
            continue;
        }

        const result = backtrack(word, position + length);

        if (result !== null) {
            return [match, ...result];
        }
    }

    return null;
}

function getPeriodicSpelling(word) {
    return backtrack(word.toLowerCase(), 0) || [];
}


console.log(getPeriodicSpelling("neon"));
console.log(getPeriodicSpelling("rational"));
console.log(getPeriodicSpelling("yarn"));
console.log(getPeriodicSpelling("carbon"));
console.log(getPeriodicSpelling("noisy"));
console.log(getPeriodicSpelling("bicycles"));
console.log(getPeriodicSpelling("optics"));
console.log(getPeriodicSpelling("value"));
