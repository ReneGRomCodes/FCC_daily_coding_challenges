/*
Schema Validator Part 4

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}

- The pipe (|) symbol means "or". role must be one of the listed Roles values.
- The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
- Extra keys are allowed

1. is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}) should return True.
2. is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}) should return True.
3. is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55})
    should return True.
4. is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}) should return False.
5. is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}) should return False.
6. is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}) should return False.
7. is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}) should return False.
8. is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}) should return False.
 */

function isValidSchema(obj) {
    const roles = new Set(["user", "creator", "moderator", "staff", "admin"])
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

    if (!roles.has(obj["role"])) {
        return false
    }

    if ("supporter" in obj) {
        if (typeof obj["supporter"] !== "boolean") {
            return false;
        }
    }

    return true
}


console.log(isValidSchema({"username": "vivian", "posts": 1, "verified": false, "role": "user", "supporter": true}));
console.log(isValidSchema({"username": "rudolph", "posts": 15, "verified": true, "role": "creator"}));
console.log(isValidSchema({"username": "hernandez", "posts": 35, "verified": true, "role": "moderator", "supporter": false, "followers": 55}));
console.log(isValidSchema({"username": "julia", "posts": 50, "verified": true, "role": "admin", "supporter": "true"}));
console.log(isValidSchema({"username": "bernard", "posts": 0, "verified": true, "role": "friend", "supporter": true}));
console.log(isValidSchema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": false}));
console.log(isValidSchema({"username": "jimmy", "posts": true, "verified": false, "role": "creator", "supporter": true}));
console.log(isValidSchema({"username": true, "posts": 30, "verified": true, "role": "moderator", "supporter": false}));
