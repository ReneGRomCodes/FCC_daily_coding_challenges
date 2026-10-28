/*
2026 Winter Games Day 14: Ski Mountaineering
Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

              |  "Shallow" | "Moderate"    | "Deep"
-------------------------------------------------
"Gentle"	  |  "Safe"	   | "Safe"	       | "Safe"
"Steep" 	  |  "Safe"	   | "Risky"	   | "Risky"
"Very Steep"  |	"Safe"	   | "Risky"	   | "Risky"

1. avalanche_risk("Shallow", "Gentle") should return "Safe".
2. avalanche_risk("Shallow", "Steep") should return "Safe".
3. avalanche_risk("Shallow", "Very Steep") should return "Safe".
4. avalanche_risk("Moderate", "Gentle") should return "Safe".
5. avalanche_risk("Moderate", "Steep") should return "Risky".
6. avalanche_risk("Moderate", "Very Steep") should return "Risky".
7. avalanche_risk("Deep", "Gentle") should return "Safe".
8. avalanche_risk("Deep", "Steep") should return "Risky".
9. avalanche_risk("Deep", "Very Steep") should return "Risky".
 */

function avalancheRisk(snowDepth, slope) {
    const risk = {
        "Shallow": {
            "Gentle": "Safe",
            "Steep": "Safe",
            "Very Steep": "Safe"
        },
        "Moderate": {
            "Gentle": "Safe",
            "Steep": "Risky",
            "Very Steep": "Risky"
        },
        "Deep": {
            "Gentle": "Safe",
            "Steep": "Risky",
            "Very Steep": "Risky"
        }
    };

    return risk[snowDepth][slope];
}

// Alternative solution. Uses a pattern I recognized, but is not as maintainable.
function avalancheRiskAlternative(snowDepth, slope) {
    if (slope === "Gentle") return "Safe";
    if (snowDepth === "Shallow") return "Safe";
    return "Risky";
}



console.log(avalancheRisk("Shallow", "Gentle"));
console.log(avalancheRisk("Shallow", "Steep"));
console.log(avalancheRisk("Shallow", "Very Steep"));
console.log(avalancheRisk("Moderate", "Gentle"));
console.log(avalancheRisk("Moderate", "Steep"));
console.log(avalancheRisk("Moderate", "Very Steep"));
console.log(avalancheRisk("Deep", "Gentle"));
console.log(avalancheRisk("Deep", "Steep"));
console.log(avalancheRisk("Deep", "Very Steep"));
