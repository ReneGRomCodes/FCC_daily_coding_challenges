"""
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
"""

def is_valid_user(user: dict) -> bool:
    roles: set[str] = {"user", "creator", "moderator", "staff", "admin"}
    schema: dict = {
        "username": str,
        "posts": int,
        "verified": bool,
        "role": str,
        "badges": list,
    }

    if not isinstance(user, dict):
        return False

    for key, expected_type in schema.items():
        if key not in user:
            return False
        if type(user[key]) is not expected_type:
            return False

    if user["role"] not in roles:
        return False

    if "supporter" in user.keys():
        if type(user["supporter"]) != bool:
            return False

    if user["badges"]:
        for item in user["badges"]:
            if type(item) != str:
                return False

    return True

def is_valid_schema(obj: dict) -> bool:

    if "users" not in obj:
        return False

    for user in obj["users"]:
        if not is_valid_user(user):
            return False

    return True


print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]},
                                 {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True,
                                  "followers": 20, "badges": ["helper"]}]}))
print(is_valid_schema({"users": []}))
print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False,
                                 "badges": []}}))
print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True,
                                  "badges": ["liked", 6]}]}))
print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false",
                                  "badges": ["comeback"]}]}))
print(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True,
                                  "badges": ["veteran"]}]}))
print(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False,
                                  "badges": ["superstar"]}]}))
print(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False,
                                  "badges": ["newbie"]}]}))
print(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False,
                                  "badges": ["superuser", "veteran"]}]}))
print(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]}))
