/*
Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

- The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
- The first string will be the time you parked your car, and the second will be the time you picked it up.
- If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.

Fee rules:
- Each hour parked costs $3.
- Partial hours are rounded up to the next full hour.
- If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
- There is a minimum fee of $5 (only used if the total would be less than $5).

Return the total cost in the format "$cost", "$5" for example.

1. calculate_parking_fee("09:00", "11:00") should return "$6".
2. calculate_parking_fee("10:00", "10:30") should return "$5".
3. calculate_parking_fee("08:10", "10:45") should return "$9".
4. calculate_parking_fee("14:40", "23:10") should return "$27".
5. calculate_parking_fee("18:15", "01:30") should return "$34".
6. calculate_parking_fee("11:11", "11:10") should return "$82".
 */

function calculateParkingFee(parkTime, pickupTime) {
    const [parkH, parkM] = parkTime.split(":").map(Number);
    const [pickH, pickM] = pickupTime.split(":").map(Number);

    let parkTotal = parkH * 60 + parkM;
    let pickTotal = pickH * 60 + pickM;

    let overnight = pickTotal < parkTotal;
    if (overnight) pickTotal += 24 * 60;

    const minutes = pickTotal - parkTotal;
    const hours = Math.ceil(minutes / 60);

    let cost = hours * 3;
    if (overnight) cost += 10;

    cost = Math.max(cost, 5);

    return `$${cost}`;
}


console.log(calculateParkingFee("09:00", "11:00"));
console.log(calculateParkingFee("10:00", "10:30"));
console.log(calculateParkingFee("08:10", "10:45"));
console.log(calculateParkingFee("14:40", "23:10"));
console.log(calculateParkingFee("18:15", "01:30"));
console.log(calculateParkingFee("11:11", "11:10"));
