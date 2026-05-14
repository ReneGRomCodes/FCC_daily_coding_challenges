/*
Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.

1. get_oldest([{ "name": "Brenda", "age": 40 }]) should return ["Brenda"].
2. get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]) should return ["Alice"].
3. get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }])
    should return ["Bill", "Carol"].
4. get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 },
    { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 },
    { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }])
        should return ["George", "Holly", "Zach"].
 */

function getOldest(people) {
    const oldestPeople = [];
    let highestAge = 0;

    for (const person of people) {
        if (!highestAge || person.age > highestAge) {
            highestAge = person.age;
        }
    }

    for (const person of people) {
        if (person.age === highestAge) {
            oldestPeople.push(person.name);
        }
    }

    return oldestPeople;
}


console.log(getOldest([{ "name": "Brenda", "age": 40 }]));
console.log(getOldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]));
console.log(getOldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]));
console.log(getOldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 },
    { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 },
    { "name": "Jennifer", "age": 43 }]));
