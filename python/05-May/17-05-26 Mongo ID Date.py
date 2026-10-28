"""
Mongo ID Date
Given a MongoDB ID string, return its creation time as an ISO 8601 string.

- A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a
base-16 integer.

For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing
a creation time of "2026-05-17T05:00:00.000Z".

1. mongo_id_to_date("6a094b50bcf86cd799439011") should return "2026-05-17T05:00:00.000Z".
2. mongo_id_to_date("695344eb1f4a4c1123042128") should return "2025-12-30T03:20:11.000Z".
3. mongo_id_to_date("386da62df34123ac54617e56") should return "2000-01-01T07:01:01.000Z".
4. mongo_id_to_date("69f571c3d7711807afd3dd55") should return "2026-05-02T03:38:43.000Z".
5. mongo_id_to_date("68adce01c0e1144d0a90295a") should return "2025-08-26T15:08:49.000Z".
"""

# Usually I avoid imports in these challenges, but without 'datetime' this entire thing would be a hilarious mess.
from datetime import datetime, timezone


def mongo_id_to_date(mongo_id: str) -> str:
    # Extract timestamp in hex and convert to seconds.
    hex_timestamp = mongo_id[:8]
    seconds = int(hex_timestamp, 16)
    # Create and format UTC datetime object.
    dt = datetime.fromtimestamp(seconds, tz=timezone.utc)

    return dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")


print(mongo_id_to_date("6a094b50bcf86cd799439011"))
print(mongo_id_to_date("695344eb1f4a4c1123042128"))
print(mongo_id_to_date("386da62df34123ac54617e56"))
print(mongo_id_to_date("69f571c3d7711807afd3dd55"))
print(mongo_id_to_date("68adce01c0e1144d0a90295a"))
