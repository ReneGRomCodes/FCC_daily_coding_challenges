"""
Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star.
Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes
in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical
values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings.
For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading
is 8 or less.

1. has_exoplanet("665544554") should return False.
2. has_exoplanet("FGFFCFFGG") should return True.
3. has_exoplanet("MONOPLONOMONPLNOMPNOMP") should return False.
4. has_exoplanet("FREECODECAMP") should return True.
5. has_exoplanet("9AB98AB9BC98A") should return False.
6. has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") should return True.
"""

def has_exoplanet(readings):

    lum_list: list[int] = [int(x, 36) for x in readings]
    lum_avrg: float = sum(lum_list) / len(lum_list)
    lum_threshold: float = lum_avrg * 0.8

    for value in lum_list:
        if value <= lum_threshold:
            return True

    return False


print(has_exoplanet("665544554"))
print(has_exoplanet("FGFFCFFGG"))
print(has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
print(has_exoplanet("FREECODECAMP"))
print(has_exoplanet("9AB98AB9BC98A"))
print(has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE"))
