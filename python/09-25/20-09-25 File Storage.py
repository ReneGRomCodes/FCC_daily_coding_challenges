"""
File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the
hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	    1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.

1. number_of_files(500, "KB", 1) should return 2000.
2. number_of_files(50000, "B", 1) should return 20000.
3. number_of_files(5, "MB", 1) should return 200.
4. number_of_files(4096, "B", 1.5) should return 366210.
5. number_of_files(220.5, "KB", 100) should return 453514.
6. number_of_files(4.5, "MB", 750) should return 166666.
"""

def number_of_files(file_size: int | float, file_unit: str, drive_size_gb: int | float) -> int:
    # Size multipliers to convert file and drive sizes to bytes.
    size_mult_kb: int = 1_000
    size_mult_mb: int = 1_000_000
    size_mult_gb: int = 1_000_000_000
    # Stores the file size in bytes.
    file_size_b: int = 0

    if file_unit == "B":
        file_size_b = file_size
    elif file_unit == "KB":
        file_size_b = file_size * size_mult_kb
    elif file_unit == "MB":
        file_size_b = file_size * size_mult_mb
    elif file_unit == "GB":  # "GB" not used in test cases. This one is here for the sake of completeness.
        file_size_b = file_size * size_mult_gb

    return int(drive_size_gb * size_mult_gb / file_size_b)


print(number_of_files(500, "KB", 1))
print(number_of_files(50000, "B", 1))
print(number_of_files(5, "MB", 1))
print(number_of_files(4096, "B", 1.5))
print(number_of_files(220.5, "KB", 100))
print(number_of_files(4.5, "MB", 750))
