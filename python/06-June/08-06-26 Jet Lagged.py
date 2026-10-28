"""
Jet Lagged
Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet
lag hours the traveller is experiencing.

The given cities will be from the following list that includes their UTC offset:
City	        Offset
"Los Angeles"	-8
"New York"	    -5
"London"	     0
"Istanbul"	    +3
"Dubai"	        +4
"Hong Kong"	    +8
"Tokyo"	        +9

To calculate jet lag hours:
1. Find the timezone difference in hours between the two cities.
2. Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
3. Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier

Return the jet lag hours rounded to one decimal place.

1. get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east") should return 6.5.
2. get_jet_lag_hours("London", "New York", 8, "west") should return 5.8.
3. get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east") should return 1.6.
4. get_jet_lag_hours("Dubai", "London", 7, "west") should return 4.7.
5. get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west") should return 17.5.
6. get_jet_lag_hours("Tokyo", "Dubai", 9, "west") should return 5.9.
7. get_jet_lag_hours("New York", "Istanbul", 10, "east") should return 9.5.
"""

def get_jet_lag_hours(departure_city: str, arrival_city: str, flight_duration: int, direction: str) -> float:
    utc_offset: dict[str, int] = {
        "los angeles": -8,
        "new york": -5,
        "london": 0,
        "istanbul": 3,
        "dubai": 4,
        "hong kong": 8,
        "tokyo": 9,
    }
    tz_difference: int = abs(utc_offset[departure_city.lower()] - utc_offset[arrival_city.lower()])
    direction_multiplier: float = 1.5 if direction.lower() == "east" else 1.0
    let_lag_hours: float = tz_difference + (flight_duration * 0.1) * direction_multiplier

    return round(let_lag_hours, 1)


print(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"))
print(get_jet_lag_hours("London", "New York", 8, "west"))
print(get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east"))
print(get_jet_lag_hours("Dubai", "London", 7, "west"))
print(get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west"))
print(get_jet_lag_hours("Tokyo", "Dubai", 9, "west"))
print(get_jet_lag_hours("New York", "Istanbul", 10, "east"))
