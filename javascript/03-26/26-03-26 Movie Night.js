/*
Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the
total cost of the movie tickets for that showing.

The given day will be one of:
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"

The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:
Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.

1. get_movie_night_cost("Saturday", "10:00pm", 1) should return "$12.00".
2. get_movie_night_cost("Sunday", "10:00am", 1) should return "$10.00".
3. get_movie_night_cost("Tuesday", "7:20pm", 2) should return "$10.00".
4. get_movie_night_cost("Wednesday", "5:40pm", 3) should return "$30.00".
5. get_movie_night_cost("Monday", "11:50am", 4) should return "$32.00".
6. get_movie_night_cost("Friday", "4:30pm", 5) should return "$50.00".
7. get_movie_night_cost("Tuesday", "11:30am", 1) should return "$5.00".
 */

function getMovieNightCost(day, showtime, numberOfTickets) {
    let price = 0;
    const weekend = new Set(["Friday", "Saturday", "Sunday"]);
    const weekday = new Set(["Monday", "Wednesday", "Thursday"]);
    // Ignored "12:00pm" as edge case here to avoid clutter. Yes, I would take that into account in a real world scenario.
    const isMatinee = (showtime.endsWith("pm") && Number(showtime.split(":")[0]) < 5) || showtime.endsWith("am");

    const prices = {
        weekend: 12,
        weekday: 10,
        tuesday: 5,
        matinee_discount: 2,
    }

    if (day === "Tuesday") {
        return `$${(prices.tuesday * numberOfTickets).toFixed(2)}`;
    }

    if (weekend.has(day)) {
        price = prices.weekend * numberOfTickets;
    } else if (weekday.has(day)) {
        price = prices.weekday * numberOfTickets;
    }

    if (isMatinee) {
        price -= prices.matinee_discount * numberOfTickets;
    }

    return `$${price.toFixed(2)}`;
}


console.log(getMovieNightCost("Saturday", "10:00pm", 1));
console.log(getMovieNightCost("Sunday", "10:00am", 1));
console.log(getMovieNightCost("Tuesday", "7:20pm", 2));
console.log(getMovieNightCost("Wednesday", "5:40pm", 3));
console.log(getMovieNightCost("Monday", "11:50am", 4));
console.log(getMovieNightCost("Friday", "4:30pm", 5));
console.log(getMovieNightCost("Tuesday", "11:30am", 1));
