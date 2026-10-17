/*
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.

1. convert_to_km(1) should return 1.61.
2. convert_to_km(21) should return 33.8.
3. convert_to_km(3.5) should return 5.63.
4. convert_to_km(0) should return 0.
5. convert_to_km(0.621371) should return 1.
 */

function convertToKm(miles) {
    let kilometers = (miles * 1.60934).toFixed(2);

    if (kilometers % 1 === 0) { return Math.floor(kilometers) }

    return kilometers;
}


console.log(convertToKm(1));
console.log(convertToKm(21));
console.log(convertToKm(3.5));
console.log(convertToKm(0));
console.log(convertToKm(0.621371));
