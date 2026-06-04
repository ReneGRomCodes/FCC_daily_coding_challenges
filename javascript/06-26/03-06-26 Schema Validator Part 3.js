/*
Schema Validator Part 3

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}

- The pipe (|) symbol means "or". role must be one of the listed Roles values.
- Extra keys are allowed

1. is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}) should return True.
2. is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}) should return True.
3. is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}) should return True.
4. is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}) should return True.
5. is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}) should return True.
6. is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}) should return False.
7. is_valid_schema({"username": "wendy", "posts": 10, "verified": True}) should return False.
8. is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}) should return False.
9. is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}) should return False.
10. is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}) should return False.
11. is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}) should return False.
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

    return roles.has(obj["role"]);
}


console.log(isValidSchema({"username": "henry", "posts": 0, "verified": true, "role": "staff"}));
console.log(isValidSchema({"username": "sara", "posts": 45, "verified": false, "role": "creator", "followers": 70}));
console.log(isValidSchema({"username": "penelope", "posts": 20, "verified": true, "role": "admin"}));
console.log(isValidSchema({"username": "kevin", "posts": 0, "verified": false, "role": "user"}));
console.log(isValidSchema({"username": "george", "posts": 15, "verified": true, "role": "moderator"}));
console.log(isValidSchema({"username": "david", "posts": 0, "verified": false, "role": "guest"}));
console.log(isValidSchema({"username": "wendy", "posts": 10, "verified": true}));
console.log(isValidSchema({"username": "fabian", "posts": 1, "verified": true, "role": true}));
console.log(isValidSchema({"username": 8, "posts": 1, "verified": true, "role": "user"}));
console.log(isValidSchema({"username": "penny", "posts": "10", "verified": true, "role": "staff"}));
console.log(isValidSchema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}));