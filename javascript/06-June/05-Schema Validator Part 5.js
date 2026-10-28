/*
Schema Validator Part 5

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"
{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

- The pipe (|) symbol means "or". role must be one of the listed Roles values.
- The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
- The brackets [] after string means that badges should be an array of strings (or empty).
- Extra keys are allowed

1. is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False,
    "badges": ["early-adopter", "popular"]})
        should return True.
2. is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True,
    "badges": ["streak-master", "veteran"], "followers": 1233})
        should return True.
3. is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []})
    should return True.
4. is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False,
    "badges": ["first-post", 18]})
        should return False.
5. is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False})
    should return False.
6. is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no",
    "badges": ["first-post", "anniversary"]})
        should return False.
7. is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True,
    "badges": ["popular"]})
        should return False.
8. is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True,
    "badges": ["helper"]})
        should return False.
9. is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]})
    should return False.
10. is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]})
    should return False.
 */

function isValidSchema(obj) {
    const roles = new Set(["user", "creator", "moderator", "staff", "admin"])
    const schema = {
        username: "string",
        posts: "number",
        verified: "boolean",
        badges: "array"
    };

    if (typeof obj !== "object" || obj === null) {
        return false;
    }

    for (const key in schema) {
        if (!(key in obj)) {
            return false;
        }

        if (schema[key] === "array") {
            if (!Array.isArray(obj[key])) {
                return false;
            }
        } else if (typeof obj[key] !== schema[key]) {
            return false;
        }
    }

    if (!roles.has(obj["role"])) {
        return false
    }

    if ("supporter" in obj) {
        if (typeof obj["supporter"] !== "boolean") {
            return false;
        }
    }

    if (obj.badges) {
        for (const item of obj.badges) {
            if (typeof item !== "string") {
                return false;
            }
        }
    }

    return true;
}


console.log(isValidSchema({"username": "gill", "posts": 12, "verified": false, "role": "creator", "supporter": false,
    "badges": ["early-adopter", "popular"]}));
console.log(isValidSchema({"username": "tonya", "posts": 299, "verified": true, "role": "moderator", "supporter": true,
    "badges": ["streak-master", "veteran"], "followers": 1233}));
console.log(isValidSchema({"username": "zara", "posts": 0, "verified": false, "role": "user", "supporter": false,
    "badges": []}));
console.log(isValidSchema({"username": "nicole", "posts": 65, "verified": true, "role": "admin", "supporter": false,
    "badges": ["first-post", 18]}));
console.log(isValidSchema({"username": "tim", "posts": 25, "verified": true, "role": "staff", "supporter": false}));
console.log(isValidSchema({"username": "charlie", "posts": 0, "verified": false, "role": "user", "supporter": "no",
    "badges": ["first-post", "anniversary"]}));
console.log(isValidSchema({"username": "wanda", "posts": 15, "verified": true, "role": "friend", "supporter": true,
    "badges": ["popular"]}));
console.log(isValidSchema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": true,
    "badges": ["helper"]}));
console.log(isValidSchema({"username": "carrie", "verified": true, "role": "moderator", "supporter": true,
    "badges": ["helper", "sharer"]}));
console.log(isValidSchema({"username": true, "posts": 75, "verified": true, "role": "creator", "supporter": true,
    "badges": ["veteran"]}));
