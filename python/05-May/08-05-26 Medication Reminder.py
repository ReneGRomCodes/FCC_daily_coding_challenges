"""
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
"""

# Medication schedule: either list of fixed times as strings or hour intervals as single integers for each medication.
MED_SCHEDULE: dict[str, list[str] | int] = {
    "Deployxitrin": ["08:00", "16:00"],
    "Debuggamanizole": ["07:00", "13:00", "21:00"],
    "Mergeflictamine": 4,
}


def time_str_to_minutes(time: str) -> int:
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])


def get_interval_schedule(scheduled_time: str, med_interval_hrs: int) -> list[int]:
    mins_per_day: int = 1440
    time_mins: int = time_str_to_minutes(scheduled_time)
    med_interval_mins: int = med_interval_hrs * 60
    schedule_mins: list[int] = []

    while time_mins - med_interval_mins >= 0:
        time_mins -= med_interval_mins

    schedule_mins.append(time_mins)

    while time_mins + med_interval_mins <= mins_per_day:
        time_mins += med_interval_mins
        schedule_mins.append(time_mins)

    return schedule_mins


def get_schedule_in_minutes_dict(medications: list[list[str]]) -> dict[str, list[int]]:
    schedule_mins: dict[str, list[int]] = {}

    for med in medications:
        medication: str = med[0]
        last_time_taken: str = med[1]
        medication_schedule: list[int] = []

        if medication in MED_SCHEDULE:
            if isinstance(MED_SCHEDULE[medication], list):
                for time in MED_SCHEDULE[medication]:
                    minutes: int = time_str_to_minutes(time)
                    medication_schedule.append(minutes)

            elif isinstance(MED_SCHEDULE[medication], int):
                medication_schedule = get_interval_schedule(last_time_taken, MED_SCHEDULE[medication])
        else:
            continue

        schedule_mins[medication] = medication_schedule

    return schedule_mins


def find_next_med_and_time(schedule: dict[str, list[int]], current_time_min: int) -> tuple[str, int, int]:
    next_med: str = ""
    next_time: int = 9999  # Random start value that's sufficiently high to get the ball rolling in the for loop below.

    for med, schedule in schedule.items():
        for time in schedule:
            time_diff: int = time - current_time_min

            if time > current_time_min and 0 < time_diff < next_time:
                next_med = med
                next_time = time_diff

    next_time_hrs: int = next_time // 60
    next_time_min: int = next_time % 60

    return next_med, next_time_hrs, next_time_min


def medication_reminder(medications: list[list[str]], current_time: str) -> str:
    medication_schedule_min: dict[str, list[int]] = get_schedule_in_minutes_dict(medications)
    current_time_min: int = time_str_to_minutes(current_time)
    next_med, next_time_hrs, next_time_min = find_next_med_and_time(medication_schedule_min, current_time_min)

    return f"{next_med} in {next_time_hrs}h {next_time_min}m"


print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]], "11:00"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "17:15"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "09:00"]], "12:59"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55"))
print(medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "07:30"]], "08:00"))
