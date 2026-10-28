/*
Blood Type Compatibility
Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.

1. can_donate("B+", "B+") should return True.
2. can_donate("O-", "AB-") should return True.
3. can_donate("O+", "A-") should return False.
4. can_donate("A+", "AB+") should return True.
5. can_donate("A-", "B-") should return False.
6. can_donate("B-", "AB+") should return True.
7. can_donate("B-", "A+") should return False.
8. can_donate("O-", "O+") should return True.
9. can_donate("O+", "O-") should return False.
10. can_donate("AB+", "AB-") should return False.
 */

function canDonate(donor, recipient) {
    const compatibilities = {
        "-": ["-", "+"],
        "+": ["+"],
        "O": ["O", "A", "B", "AB"],
        "A": ["A", "AB"],
        "B": ["B", "AB"],
        "AB": ["AB"]
    };

    const compatibleRecipients = compatibilities[donor.slice(0, -1)].concat(compatibilities[donor.slice(-1)]);

    return compatibleRecipients.includes(recipient.slice(0, -1)) && compatibleRecipients.includes(recipient.slice(-1));
}


console.log(canDonate("B+", "B+"));
console.log(canDonate("O-", "AB-"));
console.log(canDonate("O+", "A-"));
console.log(canDonate("A+", "AB+"));
console.log(canDonate("A-", "B-"));
console.log(canDonate("B-", "AB+"));
console.log(canDonate("B-", "A+"));
console.log(canDonate("O-", "O+"));
console.log(canDonate("O+", "O-"));
console.log(canDonate("AB+", "AB-"));
