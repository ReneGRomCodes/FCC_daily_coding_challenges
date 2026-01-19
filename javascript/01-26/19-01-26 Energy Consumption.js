/*
Energy Consumption
Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices
during that workout, determine which one used more energy.

To compare them, convert both values to joules using the following conversions:

1 Calorie equals 4184 joules.
1 watt-hour equals 3600 joules.
Return:

"Workout" if the workout used more energy.
"Devices" if the device used more energy.
"Equal" if both used the same amount of energy.

1. compare_energy(250, 50) should return "Workout".
2. compare_energy(100, 200) should return "Devices".
3. compare_energy(450, 523) should return "Equal".
4. compare_energy(300, 75) should return "Workout".
5. compare_energy(200, 250) should return "Devices".
6. compare_energy(900, 1046) should return "Equal".
 */

function compareEnergy(caloriesBurned, wattHoursUsed) {
    const caloriesToJoules = caloriesBurned * 4184
    const wattHoursToJoules = wattHoursUsed * 3600

    if (caloriesToJoules === wattHoursToJoules) {
        return "Equal";
    } else if (caloriesToJoules < wattHoursToJoules) {
        return "Devices";
    } else {
        return "Workout";
    }
}


console.log(compareEnergy(250, 50));
console.log(compareEnergy(100, 200));
console.log(compareEnergy(450, 523));
console.log(compareEnergy(300, 75));
console.log(compareEnergy(200, 250));
console.log(compareEnergy(900, 1046));
