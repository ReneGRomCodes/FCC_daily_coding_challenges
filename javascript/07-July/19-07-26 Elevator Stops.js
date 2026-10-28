/*
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
 */

function elevatorStops(currentFloor, stops) {
    const stopsCopy = [...stops, currentFloor];
    stopsCopy.sort((a, b) => a - b);
    const currentIndex = stopsCopy.indexOf(currentFloor);

    const distanceDown = currentFloor - stopsCopy[0];
    const distanceUp = stopsCopy[stopsCopy.length - 1] - currentFloor;
    const goesUp = distanceUp <= distanceDown;
    const downStops = stopsCopy.slice(0, currentIndex).reverse();
    const upStops = stopsCopy.slice(currentIndex + 1);

    if (goesUp) {
        return [...upStops, ...downStops];
    } else {
        return [...downStops, ...upStops];
    }
}


console.log(elevatorStops(5, [2, 8, 3, 9]));
console.log(elevatorStops(6, [2, 10, 8, 3, 1, 9]));
console.log(elevatorStops(1, [4, 8, 3, 6, 9]));
console.log(elevatorStops(12, [6, 10, 7, 3, 1, 4]));
console.log(elevatorStops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]));
