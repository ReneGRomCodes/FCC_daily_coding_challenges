"""
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
"""

def is_valid_schema(obj: dict) -> bool:
    roles: set[str] = {"user", "creator", "moderator", "staff", "admin"}
    schema: dict = {
        "username": str,
        "posts": int,
        "verified": bool,
        "role": str,
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

    return True


print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}))
print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}))
print(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}))
print(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}))
print(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}))
print(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}))
print(is_valid_schema({"username": "wendy", "posts": 10, "verified": True}))
print(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}))
print(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}))
print(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}))
print(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}))
