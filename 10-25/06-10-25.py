"""
Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself,
satellites, and your home planet in a communication route. Determine how long it will take a message sent through the
route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.

Return a number rounded to 4 decimal places, with trailing zeros removed.
1. send_message([300000, 300000]) should return 2.5.
2. send_message([384400, 384400]) should return 3.0627.
3. send_message([54600000, 54600000]) should return 364.5.
4. send_message([1000000, 500000000, 1000000]) should return 1674.3333.
5. send_message([10000, 21339, 50000, 31243, 10000]) should return 2.4086.
6. send_message([802101, 725994, 112808, 3625770, 481239]) should return 21.1597.
"""

def send_message(route) -> float:
    n_sat: int = len(route) - 1  # Number of satellites equals number of items in 'route' minus 1, as each item except the
                                 # last represents a satellite.
    trsmsn_delay: float = n_sat * 0.5
    msg_travel_time: float = (sum(route) / 300000) + trsmsn_delay

    rounded_travel_time: float = round(msg_travel_time, 4)
    travel_time_cleaned_output: float = float(str(rounded_travel_time).rstrip("0"))

    return travel_time_cleaned_output


print(send_message([300000, 300000]))
print(send_message([384400, 384400]))
print(send_message([54600000, 54600000]))
print(send_message([1000000, 500000000, 1000000]))
print(send_message([10000, 21339, 50000, 31243, 10000]))
print(send_message([802101, 725994, 112808, 3625770, 481239]))
