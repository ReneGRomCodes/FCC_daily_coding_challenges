/*
Schema Validator Part 2

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
{
  username: string,
  posts: number,
  verified: boolean
}

Extra keys are allowed.

1. is_valid_schema({"username": "alice", "posts": 10, "verified": False}) should return True.
2. is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}) should return True.
3. is_valid_schema({"username": "frank", "posts": "21", "verified": True}) should return False.
4. is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}) should return False.
5. is_valid_schema({"username": "bill", "verified": True}) should return False.
6. is_valid_schema({"username": "fred", "verified": True}) should return False.
7. is_valid_schema({"username": 5, "posts": 10, "verified": True}) should return False.
 */

function isValidSchema(obj) {
    const schema = {
        username: "string",
        posts: "number",
        verified: "boolean"
    };

    if (typeof obj !== "object" || obj === null) {
        return false;
    }

    for (const key in schema) {
        if (!(key in obj)) {
            return false;
        } if (typeof obj[key] !== schema[key]) {
            return false;
        }
    }

    return true;
}


console.log(isValidSchema({"username": "alice", "posts": 10, "verified": false}));
console.log(isValidSchema({"username": "carol", "posts": 15, "verified": true, "followers": 25}));
console.log(isValidSchema({"username": "frank", "posts": "21", "verified": true}));
console.log(isValidSchema({"username": "sam", "posts": 17, "verified": "false"}));
console.log(isValidSchema({"username": "bill", "verified": true}));
console.log(isValidSchema({"username": "fred", "verified": true}));
console.log(isValidSchema({"username": 5, "posts": 10, "verified": true}));
