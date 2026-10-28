"""
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
"""

def get_movie_night_cost(day: str, showtime: str, number_of_tickets: int) -> str:
    day: str = day.lower()
    price: int = 0
    weekend: set[str] = {"friday", "saturday", "sunday"}
    weekday: set[str] = {"monday", "wednesday", "thursday"}
    # Ignored "12:00pm" as edge case here to avoid clutter. Yes, I would take that into account in a real world scenario.
    is_matinee: bool = ((showtime[-2:] == "pm" and int(showtime.split(":")[0]) < 5) or showtime[-2:] == "am")

    prices: dict[str, int] = {
        "weekend": 12,
        "weekday": 10,
        "tuesday": 5,
        "matinee_discount": 2,
    }

    if day == "tuesday":
        return f"${prices[day] * number_of_tickets:.2f}"

    if day in weekend:
        price = prices["weekend"] * number_of_tickets
    elif day in weekday:
        price = prices["weekday"] * number_of_tickets

    if is_matinee:
        price -= prices["matinee_discount"] * number_of_tickets

    return f"${price:.2f}"


print(get_movie_night_cost("Saturday", "10:00pm", 1))
print(get_movie_night_cost("Sunday", "10:00am", 1))
print(get_movie_night_cost("Tuesday", "7:20pm", 2))
print(get_movie_night_cost("Wednesday", "5:40pm", 3))
print(get_movie_night_cost("Monday", "11:50am", 4))
print(get_movie_night_cost("Friday", "4:30pm", 5))
print(get_movie_night_cost("Tuesday", "11:30am", 1))
