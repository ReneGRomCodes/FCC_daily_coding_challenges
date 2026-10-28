/*
Roommates
Given an array of people and their roommate group, return the room assignments for a hotel stay using the following rules:

Each person has a name and a group property:
[
  { "name": "Alice", "group": "A" },
  { "name": "Bob", "group": "B" },
  { "name": "Carol", "group": "A" }
]

- People can only share a room with someone from the same group and are paired in the order they are given.
- Return an array of strings with names separated by " and " for a shared room, and just the name for a solo room. Names
  must appear in the order they were paired. For the example above, return ["Alice and Carol", "Bob"].

1. get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }])
    should return ["Alice and Carol", "Bob"].
2. get_roommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }])
    should return ["John and Julia", "Jim"].
3. get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" },
    { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }])
        should return ["Adam and Augustus", "Angelica", "Abraham and Austin", "Aaron"].
4. get_roommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" },
    { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }])
        should return ["Frank and Bailey", "Emitt", "Daria and Albert", "Charles"].
5. get_roommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" },
    { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }])
        should return ["Kevin and Yuri", "Violet and Brett", "Hugo and Wayne"].
 */

function getRoommates(people) {
    const groups = new Map();
    const result = [];

    for (const person of people) {
        const group = person.group;

        if (!groups.has(group)) {
            groups.set(group, []);
        }

        groups.get(group).push(person.name);
    }

    for (const names of groups.values()) {
        for (let i = 0; i < names.length; i += 2) {
            if (i + 1 < names.length) {
                result.push(`${names[i]} and ${names[i + 1]}`);
            } else {
                result.push(names[i]);
            }
        }
    }

    return result;
}


console.log(getRoommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }]));
console.log(getRoommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }]));
console.log(getRoommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" },
    { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]));
console.log(getRoommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" },
    { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }]));
console.log(getRoommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" },
    { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }]));
