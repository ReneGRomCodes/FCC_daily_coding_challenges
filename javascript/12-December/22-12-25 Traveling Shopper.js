/*
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	        1.00 USD
EUR	        1.10 USD
GBP	        1.25 USD
JPY	        0.0070 USD
CAD	        0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order
given.

1. buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) should return "Buy the first 2 items.".
2. buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) should return "Buy them all!".
3. buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]])
    should return "Buy the first 3 items.".
4. buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]])
    should return "Buy them all!".
5. buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]])
    should return "Buy the first 5 items.".
 */

function buyItems(funds, items) {
    const exchangeRatesUsd = {
        "eur": 1.1,
        "gbp": 1.25,
        "jpy": 0.007,
        "cad": 0.75,
    };

    const itemsUsd = [];
    let itemsUsdSum = 0.0;
    let fundsUsd = 0;
    const buyList = [];

    if (funds[1] !== "USD") { fundsUsd = Number(funds[0]) * exchangeRatesUsd[funds[1].toLowerCase()] }
    else { fundsUsd = Number(funds[0]) }

    for (const item of items) {
        let price = Number(item[0]);
        const currency = item[1].toLowerCase();

        if (currency !== "usd") { price = price * exchangeRatesUsd[currency] }

        itemsUsd.push(price);
    }

    for (const item of itemsUsd) {
        const newUsdSum = itemsUsdSum + item;

        if (newUsdSum <= fundsUsd) {
            itemsUsdSum = newUsdSum;
            buyList.push(item);
        } else { break }
    }

    if (buyList.length === itemsUsd.length) { return "Buy them all!" }
    else { return `Buy the first ${buyList.length} items.` }
}



console.log(buyItems(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]));
console.log(buyItems(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]));
console.log(buyItems(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]));
console.log(buyItems(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]));
console.log(buyItems(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]));
