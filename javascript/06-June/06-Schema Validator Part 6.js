/*
Schema Validator Part 6

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}

- The pipe (|) symbol means "or". role must be one of the listed Roles values.
- The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
- UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
- Extra keys are allowed

1. is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]},
    {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]})
        should return True.
2. is_valid_schema({"users": []}) should return True.
3. is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}})
    should return False.
4. is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True,
    "badges": ["liked", 6]}]}) should return False.
5. is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false",
    "badges": ["comeback"]}]}) should return False.
6. is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True,
    "badges": ["veteran"]}]}) should return False.
7. is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False,
    "badges": ["superstar"]}]}) should return False.
8. is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False,
    "badges": ["newbie"]}]}) should return False.
9. is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser",
    "veteran"]}]}) should return False.
10. is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True,
    "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True,
    "badges": ["first"]}, {}]}) should return False.
 */

function isValidUser(user) {
    const roles = new Set(["user", "creator", "moderator", "staff", "admin"])
    const schema = {
        username: "string",
        posts: "number",
        verified: "boolean",
        badges: "array"
    };

    if (typeof user !== "object" || user === null) {
        return false;
    }

    for (const key in schema) {
        if (!(key in user)) {
            return false;
        }

        if (schema[key] === "array") {
            if (!Array.isArray(user[key])) {
                return false;
            }
        } else if (typeof user[key] !== schema[key]) {
            return false;
        }
    }

    if (!roles.has(user["role"])) {
        return false
    }

    if ("supporter" in user) {
        if (typeof user["supporter"] !== "boolean") {
            return false;
        }
    }

    if (user.badges) {
        for (const item of user.badges) {
            if (typeof item !== "string") {
                return false;
            }
        }
    }

    return true;
}


function isValidSchema(obj) {
    if (typeof obj !== "object" || obj === null) {
        return false;
    }

    if (!("users" in obj)) {
        return false;
    }

    if (!Array.isArray(obj.users)) {
        return false;
    }

    for (const user of obj.users) {
        if (!isValidUser(user)) {
            return false;
        }
    }

    return true;
}

console.log(isValidSchema({"users": [{"username": "ron", "posts": 14, "verified": true, "role": "creator", "badges": ["early-adopter"]},
        {"username": "cher", "posts": 25, "verified": true, "role": "moderator", "supporter": true, "followers": 20, "badges": ["helper"]}]}));
console.log(isValidSchema({"users": []}));
console.log(isValidSchema({"users": {"username": "anne", "posts": 0, "verified": false, "role": "user", "supporter": false, "badges": []}}));
console.log(isValidSchema({"users": [{"username": "tony", "posts": 10, "verified": true, "role": "creator", "supporter": true, "badges": ["liked", 6]}]}));
console.log(isValidSchema({"users": [{"username": "ursula", "posts": 3, "verified": false, "role": "user", "supporter": "false", "badges": ["comeback"]}]}));
console.log(isValidSchema({"users": [{"username": "benny", "posts": 55, "verified": true, "role": "superstar", "supporter": true, "badges": ["veteran"]}]}));
console.log(isValidSchema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": false, "badges": ["superstar"]}]}));
console.log(isValidSchema({"users": [{"username": "carla", "posts": "10", "verified": false, "role": "user", "supporter": false, "badges": ["newbie"]}]}));
console.log(isValidSchema({"users": [{"posts": 4, "verified": false, "role": "admin", "supporter": false, "badges": ["superuser", "veteran"]}]}));
console.log(isValidSchema({"users": [{"username": "harold", "posts": 80, "verified": true, "role": "creator", "supporter": true, "badges": ["liked", "hero"]},
        {"username": "kim", "posts": 11, "verified": false, "role": "admin", "supporter": true, "badges": ["first"]}, {}]}));
