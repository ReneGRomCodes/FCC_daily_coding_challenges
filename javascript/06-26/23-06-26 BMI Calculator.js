/*
BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.

To get BMI: divide the weight by the height squared, then multiply the result by 703.

1. calculate_bmi(180, 70) should return 25.8.
2. calculate_bmi(140, 64) should return 24.0.
3. calculate_bmi(160, 76) should return 19.5.
4. calculate_bmi(200, 60) should return 39.1.
5. calculate_bmi(150, 68) should return 22.8.
 */

function calculateBmi(weight, height) {
    return ((weight / height**2) * 703).toFixed(1);
}


console.log(calculateBmi(180, 70));
console.log(calculateBmi(140, 64));
console.log(calculateBmi(160, 76));
console.log(calculateBmi(200, 60));
console.log(calculateBmi(150, 68));
