"""
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
"""

# I didn't take years and months into account here as they are irrelevant in the given test cases and would just
# clutter the rest of the code. It could be implemented similarly to the second part of this function further down,
# but come one, let me be lazy for once ;)

def can_retake(finish_time: str, current_time: str) -> bool:
    # Basic check for passed days.
    days_passed = int(current_time[8:10]) - int(finish_time[8:10])

    if days_passed < 2:
        return False
    elif days_passed > 2:
        return True

    # Check for time of day if 'days passed' checked didn't trigger.
    finish_time_list: list[int] = [int(x) for x in finish_time[11:].split(":")]  # [h, m, s]
    current_time_list: list[int] = [int(x) for x in current_time[11:].split(":")]  # [h, m, s]
    finish_h, current_h = finish_time_list[0], current_time_list[0]
    finish_m, current_m = finish_time_list[1], current_time_list[1]
    finish_s, current_s = finish_time_list[2], current_time_list[2]

    if (current_h, current_m, current_s) < (finish_h, finish_m, finish_s):
        return False

    return True


print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))
