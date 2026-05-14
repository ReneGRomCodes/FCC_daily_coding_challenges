"""
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
"""

def get_oldest(people: list[dict[str, str | int]]) -> list[str]:
    oldest_people: list[str] = []
    highest_age: int = 0

    # Find highest age.
    for person in people:
        if not highest_age or person["age"] > highest_age:
            highest_age = person["age"]

    # Find oldest people.
    for person in people:
        if person["age"] == highest_age:
            oldest_people.append(person["name"])

    return oldest_people


print(get_oldest([{ "name": "Brenda", "age": 40 }]))
print(get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]))
print(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]))
print(get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 },
                  { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 },
                  { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))
