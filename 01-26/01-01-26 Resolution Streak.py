"""
Resolution Streak
Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three
integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that
day; determine if you are keeping your resolutions.

The first sub-array is day 1, and second day 2, and so on.
A day is considered successful if all three of the following goals are met:

You walked at least 10,000 steps.
You had no more than 120 minutes of screen time.
You read at least five pages.
If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful
days.

If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of
the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.

1. resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]) should return "Resolution on track: 3 day streak."
2. resolution_streak([[10000, 120, 5], [10950, 121, 11]]) should return "Resolution failed on day 2: 1 day streak."
3. resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]])
    should return "Resolution failed on day 3: 2 day streak."
4. resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]])
    should return "Resolution failed on day 4: 3 day streak."
5. resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13],
                      [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]])
    should return "Resolution on track: 10 day streak."
"""

def resolution_streak(days: list[list[int]]) -> str:
    for day, goals in enumerate(days, start=1):
        # Check for failed goals.
        steps: bool = goals[0] < 10000
        screen_time: bool = goals[1] > 120
        pages_read: bool = goals[2] < 5

        if steps or screen_time or pages_read:
            return f"Resolution failed on day {day}: {day-1} day streak."

    return f"Resolution on track: {len(days)} day streak."


print(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]))
print(resolution_streak([[10000, 120, 5], [10950, 121, 11]]))
print(resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]))
print(resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]))
print(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9],
                         [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]))
