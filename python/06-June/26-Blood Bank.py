"""
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
"""

def serve_patient(patient: str, bank: list[str]) -> int:
    if patient == "AB":  # 'AB' is compatible with every blood type, so just chug in whatever is in stock.
        bank.pop()
    else:
        bank.remove(patient)

    return 1


def triage_blood(bank: list[str], patients: list[str]) -> str:
    """NOTE: Usually I would map the bank inventory to a dict, which would be less computationally heavy. But because
    of the small scale of this challenge I decided to go for a more straight forward iteration approach which makes this
    thing a bit more readable."""
    n_patients: int = len(patients)
    patients_served: int = 0

    # Patient sorted by blood types and general compatibility ('O' least compatible to 'AB' most compatible).
    sorted_types: tuple[list[str], ...] = ([x for x in patients if x == "O"], [x for x in patients if x == "A"],
                                           [x for x in patients if x == "B"], [x for x in patients if x == "AB"])

    for type_group in sorted_types:
        for patient in type_group:
            has_bank_patient: bool = patient in bank

            if patient == "O" and has_bank_patient:
                patients_served += serve_patient(patient, bank)
            elif patient in ("A", "B"):
                if has_bank_patient:
                    patients_served += serve_patient(patient, bank)
                elif "O" in bank:
                    patients_served += serve_patient("O", bank)
            elif patient == "AB" and bank:
                patients_served += serve_patient(patient, bank)

    return f"{patients_served} of {n_patients} patients served"


print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]))
print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]))
print(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]))
print(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"],
                   ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]))
