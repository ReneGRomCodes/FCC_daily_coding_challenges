"""
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
"""


def is_valid_schema(obj: dict) -> bool:
    schema: dict = {
        "username": str,
        "posts": int,
        "verified": bool,
    }

    if not isinstance(obj, dict):
        return False

    for key, expected_type in schema.items():
        if key not in obj:
            return False

        if type(obj[key]) is not expected_type:
            return False

    return True


print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))
print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}))
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))
print(is_valid_schema({"username": "bill", "verified": True}))
print(is_valid_schema({"username": "fred", "verified": True}))
print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))
