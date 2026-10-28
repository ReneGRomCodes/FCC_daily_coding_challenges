/*
Acronym Finder
Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

- "National Avocado Storage Authority"
- "Cats Infiltration Agency"
- "Fluffy Beanbag Inspectors"
- "Department Of Jelly"
- "Wild Honey Organization"
- "Eating Pancakes Administration"

Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the
same order.

1. find_org("NASA") should return "National Avocado Storage Authority".
2. find_org("CIA") should return "Cats Infiltration Agency".
3. find_org("FBI") should return "Fluffy Beanbag Inspectors".
4. find_org("DOJ") should return "Department Of Jelly".
5. find_org("WHO") should return "Wild Honey Organization".
6. find_org("EPA") should return "Eating Pancakes Administration".
 */

function findOrg(acronym) {
    const acronyms = {
        NASA: "National Avocado Storage Authority",
        CIA: "Cats Infiltration Agency",
        FBI: "Fluffy Beanbag Inspectors",
        DOJ: "Department Of Jelly",
        WHO: "Wild Honey Organization",
        EPA: "Eating Pancakes Administration",
    }

    return acronyms[acronym.toUpperCase()];
}


console.log(findOrg("NASA"));
console.log(findOrg("CIA"));
console.log(findOrg("FBI"));
console.log(findOrg("DOJ"));
console.log(findOrg("WHO"));
console.log(findOrg("EPA"));
