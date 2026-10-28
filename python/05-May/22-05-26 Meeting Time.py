"""
Meeting Time
Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one
hour free. If no such time exists, return "None".

- Each person's availability is an array of [start, end] integer pairs in 24-hour time. For example, [10, 12] would mean
  the person is available from 10 to 12. Start times range from 0-23, and end times range from 1-24.

For example, given:
[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]

Return 11, the start of their first shared free hour.

1. get_meeting_time([[[10, 12], [15, 16]], [[11, 14], [15, 16]]]) should return 11.
2. get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]]) should return 13.
3. get_meeting_time([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]]) should return 9.
4. get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]])
    should return None.
5. get_meeting_time([[[1, 3], [4, 6], [8, 10], [20, 23]], [[15, 16], [17, 18], [19, 22], [23, 24]], [[14, 16], [17, 23]],
    [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]]) should return 21.
"""

def get_meeting_time(availability: list[list[list[int]]]) -> int | str:
    timeline_map: list[int] = [0 for _ in range(0, 24)]
    n_people: int = len(availability)

    for person in availability:
        # Set to ensure no hour is counted twice... I see what you did there test case 2.
        hours: set[int] = set()

        for window in person:
            start, end = window

            for hour in range(start, end):
                if not hour in hours:
                    timeline_map[hour] += 1
                    hours.add(hour)

    if n_people in timeline_map:
        return timeline_map.index(n_people)
    else:
        return "None"


print(get_meeting_time([
    [[10, 12], [15, 16]],
    [[11, 14], [15, 16]]
]))
print(get_meeting_time([
    [[9, 10], [12, 15]],
    [[10, 11], [13, 14]],
    [[9, 11], [10, 14]]
]))
print(get_meeting_time([
    [[7, 8], [9, 11], [12, 14], [15, 16]],
    [[8, 11], [12, 13], [14, 15]]
]))
print(get_meeting_time([
    [[7, 8], [10, 12], [13, 15]],
    [[8, 11], [12, 13], [14, 15]],
    [[6, 7], [8, 9], [12, 13]]
]))
print(get_meeting_time([
    [[1, 3], [4, 6], [8, 10], [20, 23]],
    [[15, 16], [17, 18], [19, 22], [23, 24]],
    [[14, 16], [17, 23]],
    [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]
]))
