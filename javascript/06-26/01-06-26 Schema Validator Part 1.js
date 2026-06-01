/*

Schema Validator Part 1

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
{
    username: string
}

Extra keys are allowed.

1. is_valid_schema({"username": "bob"}) should return True.
2. is_valid_schema({"username": "jen", "posts": 30}) should return True.
3. is_valid_schema({"username": ""}) should return True.
4. is_valid_schema({"username": 7}) should return False.
5. is_valid_schema({"posts": 25}) should return False.
 */

function isValidSchema(obj) {
    if (typeof obj !== "object" || obj === null) {
        return false;
    } else if (!("username" in obj)) {
        return false;
    } else if (typeof obj.username !== "string") {
        return false;
    }

    return true;
}


console.log(isValidSchema({"username": "bob"}));
console.log(isValidSchema({"username": "jen", "posts": 30}));
console.log(isValidSchema({"username": ""}));
console.log(isValidSchema({"username": 7}));
console.log(isValidSchema({"posts": 25}));
