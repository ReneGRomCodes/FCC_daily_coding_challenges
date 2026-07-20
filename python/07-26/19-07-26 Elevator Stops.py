"""
Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the
elevator should visit them to minimize number of floors traveled.

- If tied, go up first
- Floors with a request must be visited when the elevator first passes them

1. elevator_stops(5, [2, 8, 3, 9]) should return [3, 2, 8, 9].
2. elevator_stops(6, [2, 10, 8, 3, 1, 9]) should return [8, 9, 10, 3, 2, 1].
3. elevator_stops(1, [4, 8, 3, 6, 9]) should return [3, 4, 6, 8, 9].
4. elevator_stops(12, [6, 10, 7, 3, 1, 4]) should return [10, 7, 6, 4, 3, 1].
5. elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]) should return [10, 9, 8, 6, 5, 2, 12, 19, 23].
"""

def elevator_stops(current_floor: int, stops: list[int]) -> list[int]:
    stops_copy: list[int] = stops.copy()
    stops_copy.append(current_floor)
    stops_copy.sort()

    current_floor_index: int = stops_copy.index(current_floor)
    distance_down, distance_up = current_floor - stops_copy[0], stops_copy[-1] - current_floor
    goes_up: bool = distance_up <= distance_down
    down_stops, up_stops = stops_copy[:current_floor_index][::-1], stops_copy[current_floor_index + 1:]

    if goes_up:
        return up_stops + down_stops
    else:
        return down_stops + up_stops


print(elevator_stops(5, [2, 8, 3, 9]))
print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
print(elevator_stops(1, [4, 8, 3, 6, 9]))
print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))
