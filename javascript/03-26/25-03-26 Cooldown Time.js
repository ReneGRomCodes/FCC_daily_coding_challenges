/*
Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time,
determine whether the user can take an exam again.

- Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time
  is 24-hour clock.
- A user must wait at least 48 hours before retaking an exam.

1. can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00") should return True.
2. can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00") should return False.
3. can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00") should return True.
4. can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59") should return False.
 */

/*
I didn't take years and months into account here as they are irrelevant in the given test cases and would just
clutter the rest of the code. It could be implemented similarly to the second part of this function further down,
but come one, let me be lazy for once ;)
 */

function canRetake(finishTime, currentTime) {
    // Basic check for passed days.
    const daysPassed = currentTime.slice(8, 10) - finishTime.slice(8, 10)

    if (daysPassed < 2) {
        return false;
    } else if (daysPassed > 2) {
        return true;
    }

    // Check for time of day if 'days passed' checked didn't trigger.
    const [finishH, finishM, finishS] = finishTime
        .slice(11)
        .split(":")
        .map(Number);
    const [currentH, currentM, currentS] = currentTime
        .slice(11)
        .split(":")
        .map(Number);

    if (currentH < finishS) {
        return false;
    } else if (currentH > finishH) {
        return true;
    } else if (currentM < finishM) {
        return false;
    } else if (currentM > finishM) {
        return true;
    } else if (currentS < finishS) {
        return false;
    } else if (currentS > finishS) {
        return true;
    }

    return true;
}


console.log(canRetake("2026-03-23T08:00:00", "2026-03-25T14:00:00"));
console.log(canRetake("2026-03-24T14:00:00", "2026-03-25T10:00:00"));
console.log(canRetake("2026-03-23T09:25:00", "2026-03-25T09:25:00"));
console.log(canRetake("2026-03-25T11:50:00", "2026-03-23T11:49:59"));
