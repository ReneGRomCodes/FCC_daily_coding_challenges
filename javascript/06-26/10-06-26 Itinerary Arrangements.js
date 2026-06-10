/*
Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.

The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional
stops can be placed anywhere in the itinerary, subject to the following rules:

- "breakfast" is always first, with at least one stop before "lunch".
- "lunch" must appear before "dinner", with at least one stop in between.
- At most, one optional stop may appear after "dinner".

Return the number of valid arrangements.

1. get_itinerary_count(["library", "park"]) should return 2.
2. get_itinerary_count(["library", "park", "arcade"]) should return 18.
3. get_itinerary_count(["library", "park", "arcade", "store"]) should return 120.
4. get_itinerary_count(["library", "park", "arcade", "store", "cafe"]) should return 840.
5. get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]) should return 55440.
 */

function getItineraryCount(stops) {
    const nStops = stops.length;

    let factorial = 1;
    for (let i = 1; i <= nStops; i++) {
        factorial *= i;
    }

    return (2 * nStops - 3) * factorial;
}


console.log(getItineraryCount(["library", "park"]));
console.log(getItineraryCount(["library", "park", "arcade"]));
console.log(getItineraryCount(["library", "park", "arcade", "store"]));
console.log(getItineraryCount(["library", "park", "arcade", "store", "cafe"]));
console.log(getItineraryCount(["library", "park", "arcade", "store", "cafe", "market", "museum"]));
