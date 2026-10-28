"""
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
"""

def is_valid_schema(obj: dict) -> bool:
    roles: set[str] = {"user", "creator", "moderator", "staff", "admin"}
    schema: dict = {
        "username": str,
        "posts": int,
        "verified": bool,
        "role": str,
        "badges": list,
    }

    if not isinstance(obj, dict):
        return False

    for key, expected_type in schema.items():
        if key not in obj:
            return False
        if type(obj[key]) is not expected_type:
            return False

    if obj["role"] not in roles:
        return False

    if "supporter" in obj.keys():
        if type(obj["supporter"]) != bool:
            return False

    if obj["badges"]:
        for item in obj["badges"]:
            if type(item) != str:
                return False

    return True


print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False,
                       "badges": ["early-adopter", "popular"]}))
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True,
                       "badges": ["streak-master", "veteran"], "followers": 1233}))
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False,
                       "badges": []}))
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False,
                       "badges": ["first-post", 18]}))
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}))
print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no",
                       "badges": ["first-post", "anniversary"]}))
print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True,
                       "badges": ["popular"]}))
print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True,
                       "badges": ["helper"]}))
print(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True,
                       "badges": ["helper", "sharer"]}))
print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True,
                       "badges": ["veteran"]}))
