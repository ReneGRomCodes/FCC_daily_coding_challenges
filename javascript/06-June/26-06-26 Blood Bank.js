/*
Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the
format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's
inventory, and Y is the total number of patients.

Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".

Compatibility rules:
- "AB" can receive from any blood type.
- "A" can receive from "A" and "O".
- "B" can receive from "B" and "O".
- "O" can only receive from "O".

Duplicate entries in the given arrays represent quantity.

1. triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
2. triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]) should return "3 of 5 patients served".
3. triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]) should return "4 of 5 patients served".
4. triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
5. triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"])
    should return "8 of 11 patients served".
6. triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"],
    ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]) should return "13 of 14 patients served".
 */

function servePatient(patient, bank) {
    if (patient === "AB") {
        // 'AB' is compatible with every blood type, so just chug in whatever is in stock.
        bank.pop();
    } else {
        const index = bank.indexOf(patient);
        if (index > -1) {
            bank.splice(index, 1);
        }
    }
    return 1;
}


function triageBlood(bank, patients) {
    /*
    NOTE: Usually I would map the bank inventory to an object, which would be less computationally heavy. But because of
    the small scale of this challenge I decided to go for a more straight forward iteration approach which makes this
    thing a bit more readable.
     */
    const nPatients = patients.length;
    let patientsServed = 0;

    // Patient sorted by blood types and general compatibility ('O' least compatible to 'AB' most compatible).
    const sortedTypes = [
        patients.filter(x => x === "O"),
        patients.filter(x => x === "A"),
        patients.filter(x => x === "B"),
        patients.filter(x => x === "AB")
    ];

    for (const typeGroup of sortedTypes) {
        for (const patient of typeGroup) {
            const hasBankPatient = bank.includes(patient);

            if (patient === "O" && hasBankPatient) {
                patientsServed += servePatient(patient, bank);
            } else if (patient === "A" || patient === "B") {
                if (hasBankPatient) {
                    patientsServed += servePatient(patient, bank);
                } else if (bank.includes("O")) {
                    patientsServed += servePatient("O", bank);
                }
            } else if (patient === "AB" && bank.length > 0) {
                patientsServed += servePatient(patient, bank);
            }
        }
    }

    return `${patientsServed} of ${nPatients} patients served`;
}


console.log(triageBlood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]));
console.log(triageBlood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]));
console.log(triageBlood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]));
console.log(triageBlood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]));
console.log(triageBlood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]));
console.log(triageBlood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"],
    ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]));
