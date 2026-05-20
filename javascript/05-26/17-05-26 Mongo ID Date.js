/*
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
 */

function mongoIdToDate(mongoId) {
    // Extract timestamp in hex and convert to seconds.
    const hexTimestamp = mongoId.slice(0, 8);
    const seconds = parseInt(hexTimestamp, 16);
    // Create Date object (multiply by 1000, because JS expects milliseconds).
    const date = new Date(seconds * 1000);

    return date.toISOString();
}


console.log(mongoIdToDate("6a094b50bcf86cd799439011"));
console.log(mongoIdToDate("695344eb1f4a4c1123042128"));
console.log(mongoIdToDate("386da62df34123ac54617e56"));
console.log(mongoIdToDate("69f571c3d7711807afd3dd55"));
console.log(mongoIdToDate("68adce01c0e1144d0a90295a"));
