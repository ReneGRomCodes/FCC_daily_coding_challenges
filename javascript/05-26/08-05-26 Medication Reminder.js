/*
Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take
and how long until you need to take it.

- Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time
  it was last taken.
- All given times will be in "HH:MM" (24-hour) format.

Use the following medication schedule:
Name	            Schedule
Deployxitrin	    08:00, 16:00
Debuggamanizole	    07:00, 13:00, 21:00
Mergeflictamine	    every 4 hours

Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".

1. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00")
    should return "Debuggamanizole in 2h 0m".
2. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55")
    should return "Deployxitrin in 1h 5m".
3. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15")
    should return "Mergeflictamine in 0h 45m".
4. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59")
    should return "Debuggamanizole in 0h 1m".
5. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55")
    should return "Debuggamanizole in 0h 5m".
6. medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00")
    should return "Mergeflictamine in 3h 30m".
 */

// Medication schedule: either list of fixed times as strings or hour intervals as single integers for each medication.
const MED_SCHEDULE = {
    Deployxitrin: ["08:00", "16:00"],
    Debuggamanizole: ["07:00", "13:00", "21:00"],
    Mergeflictamine: 4,
};


const timeToMins = (timeStr) => {
    const [hrs, mins] = timeStr.split(":").map(Number);
    return hrs * 60 + mins;
};


function medicationReminder(medications, currentTime) {
    const nowMins = timeToMins(currentTime);

    const allUpcomingDoses = medications.flatMap(([name, lastTaken]) => {
        let scheduleMins = [];

        if (Array.isArray(MED_SCHEDULE[name])) {
            scheduleMins = MED_SCHEDULE[name].map(timeToMins);
        } else {
            const intervalMins = MED_SCHEDULE[name] * 60;
            let start = timeToMins(lastTaken);

            while (start >= intervalMins) start -= intervalMins;

            for (let t = start; t < 1440; t += intervalMins) {
                scheduleMins.push(t);
            }
        }

        return scheduleMins
            .map(doseTime => ({ name, waitTime: doseTime - nowMins }))
            .filter(dose => dose.waitTime > 0);
    });

    const nextDose = allUpcomingDoses.reduce((prev, curr) =>
        curr.waitTime < prev.waitTime ? curr : prev
    );

    const h = Math.floor(nextDose.waitTime / 60);
    const m = nextDose.waitTime % 60;

    return `${nextDose.name} in ${h}h ${m}m`;
}


console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"));
console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"));
console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"));
console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"));
console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"));
console.log(medicationReminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"));
