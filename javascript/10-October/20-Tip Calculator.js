/*
Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom
amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].

1. calculate_tips("$10.00", "25%") should return ["$1.50", "$2.00", "$2.50"].
2. calculate_tips("$89.67", "26%") should return ["$13.45", "$17.93", "$23.31"].
3. calculate_tips("$19.85", "9%") should return ["$2.98", "$3.97", "$1.79"].
 */

function calculateTips(mealPrice, customTip) {
    mealPrice = Number(mealPrice.slice(1));
    customTip = Number(customTip.slice(0, -1));
    const tipValues = [15, 20, customTip];
    const priceWithTip = [];

    for (const value of tipValues) { priceWithTip.push(`$${(mealPrice / 100 * value).toFixed(2)}`) }

    return priceWithTip;
}


console.log(calculateTips("$10.00", "25%"));
console.log(calculateTips("$89.67", "26%"));
console.log(calculateTips("$19.85", "9%"));
