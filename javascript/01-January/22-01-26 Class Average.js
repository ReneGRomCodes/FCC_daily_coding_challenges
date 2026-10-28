/*
Class Average
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following
chart:

Average Score	Letter Grade
97-100	        "A+"
93-96	        "A"
90-92	        "A−"
87-89	        "B+"
83-86	        "B"
80-82	        "B-"
77-79	        "C+"
73–76	        "C"
70-72	        "C-"
67-69	        "D+"
63-66	        "D"
60–62	        "D-"
below 60	    "F"
Calculate the average by adding all scores in the array and dividing by the total number of scores.

1. get_average_grade([92, 91, 90, 94, 89, 93]) should return "A-".
2. get_average_grade([84, 89, 85, 100, 91, 88, 79]) should return "B+".
3. get_average_grade([63, 69, 65, 66, 71, 64, 65]) should return "D".
4. get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]) should return "A+".
5. get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]) should return "C+".
6. get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]) should return "F".
 */

function getAverageGrade(scores) {
    const grades = {
        "A+": [97, 100],
        "A": [93, 96],
        "A-": [90, 92],
        "B+": [87, 89],
        "B": [83, 86],
        "B-": [80, 82],
        "C+": [77, 79],
        "C": [73, 76],
        "C-": [70, 72],
        "D+": [67, 69],
        "D": [63, 66],
        "D-": [60, 62],
        "F": [0, 59],
    };

    const avrgScore = Math.floor(scores.reduce((a, b) => a + b, 0) / scores.length);

    for (const [grade, [min, max]] of Object.entries(grades)) {
        if (min <= avrgScore && avrgScore <= max) {
            return grade;
        }
    }
}


console.log(getAverageGrade([92, 91, 90, 94, 89, 93]));
console.log(getAverageGrade([84, 89, 85, 100, 91, 88, 79]));
console.log(getAverageGrade([63, 69, 65, 66, 71, 64, 65]));
console.log(getAverageGrade([97, 98, 99, 100, 96, 97, 98, 99, 100]));
console.log(getAverageGrade([75, 100, 88, 79, 80, 78, 64, 60]));
console.log(getAverageGrade([45, 48, 50, 52, 100, 54, 56, 58, 59]));
