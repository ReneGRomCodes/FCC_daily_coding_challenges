/*
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
 */

function numberOfFiles(fileSize, fileUnit, driveSizeGb) {
    // Size multipliers to convert file and drive sizes to bytes.
    const sizeMultKb = 1_000;
    const sizeMultMb = 1_000_000;
    const sizeMultGb = 1_000_000_000;
    //Stores the file size in bytes.
    let fileSizeB = 0;

    if (fileUnit === "B") { fileSizeB = fileSize }
    else if (fileUnit === "KB") { fileSizeB = fileSize * sizeMultKb }
    else if (fileUnit === "MB") { fileSizeB = fileSize * sizeMultMb }
    // "GB" not used in test cases. This one is here for the sake of completeness.
    else if (fileUnit === "GB") { fileSizeB = fileSize * sizeMultGb }

    return Math.floor(driveSizeGb * sizeMultGb / fileSizeB);
}


console.log(numberOfFiles(500, "KB", 1))
console.log(numberOfFiles(50000, "B", 1))
console.log(numberOfFiles(5, "MB", 1))
console.log(numberOfFiles(4096, "B", 1.5))
console.log(numberOfFiles(220.5, "KB", 100))
console.log(numberOfFiles(4.5, "MB", 750))
