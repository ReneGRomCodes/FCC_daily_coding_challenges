/*
Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's
score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par.

1. golf_score(3, 3) should return "Par".
2. golf_score(4, 3) should return "Birdie".
3. golf_score(3, 1) should return "Hole in one!".
4. golf_score(5, 7) should return "Double bogey".
5. golf_score(4, 5) should return "Bogey".
6. golf_score(5, 3) should return "Eagle".
 */

function golfScore(par, strokes) {
    const scoreObj = {
        "Hole in one!": strokes === 1,
        "Eagle": strokes === par-2,
        "Birdie": strokes === par-1,
        "Par": strokes === par,
        "Bogey": strokes === par+1,
        "Double bogey": strokes === par+2
    }

    for (const [k, v] of Object.entries(scoreObj)) {
        if (v) { return k }
    }
}


console.log(golfScore(3, 3));
console.log(golfScore(4, 3));
console.log(golfScore(3, 1));
console.log(golfScore(5, 7));
console.log(golfScore(4, 5));
console.log(golfScore(5, 3));
