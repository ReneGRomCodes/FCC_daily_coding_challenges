"""
2026 Winter Games Day 17: Closing Day
Given a 2D array of medal winners, return a medal count for each country as a CSV string.

In the given array, each sub-array represents a single event: [gold_winner, silver_winner, bronze_winner]

The returned CSV string should have the following format, with the first line being headers:

Country,Gold,Silver,Bronze,Total
country_name,gold_count,silver_count,bronze_count,total_medals
Separate new lines with the new line character ("\n").
Do not include spaces around commas or at the end of lines.
Sort the returned CSV by gold medal count, highest first. If two countries have the same gold medal count, sort the tied ones alphabetically.
For example, given:

[
  ["USA", "CAN", "NOR"],
  ["NOR", "USA", "CAN"],
  ["USA", "NOR", "SWE"]
]

Return:
"Country,Gold,Silver,Bronze,Total\n
USA,2,1,0,3\n
NOR,1,1,1,3\n
CAN,0,1,1,2\n
SWE,0,0,1,1"

Which looks like this when printed:
Country,Gold,Silver,Bronze,Total
USA,2,1,0,3
NOR,1,1,1,3
CAN,0,1,1,2
SWE,0,0,1,1

1. count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]])
    should return "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1".
2. count_medals([["NOR","SWE","FIN"]])
    should return "Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1".
3. count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]])
    should return "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2".
4. count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]])
    should return "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2".
5. count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]])
    should return "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2".
6. count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]])
    should return "Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2".
"""

def count_medals(winners: list[list[str]]) -> str:
    medals_by_country: dict[str, list[int]] = {}

    for event in winners:
        for i, country in enumerate(event):
            if country not in medals_by_country.keys():
                medals_by_country[country] = [0, 0, 0, 0]

            medals_by_country[country][i] += 1  # Gold/Silve/Bronze.
            medals_by_country[country][3] += 1  # Total.

    # Sort by Gold descending, then alphabetically.
    sorted_items = sorted(
        medals_by_country.items(),
        key=lambda item: (-item[1][0], item[0])
    )

    # Build CSV.
    lines = ["Country,Gold,Silver,Bronze,Total"]

    for country, medals in sorted_items:
        gold, silver, bronze, total = medals
        lines.append(f"{country},{gold},{silver},{bronze},{total}")

    return "\n".join(lines)


print(count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]))
print(count_medals([["NOR","SWE","FIN"]]))
print(count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]))
print(count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"],
                    ["FRA","GER","ITA"]]))
print(count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"],
                    ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]))
print(count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"],
                    ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"],
                    ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]))
