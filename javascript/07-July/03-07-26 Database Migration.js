/*
Database Migration
Given two database objects, return the second object with any missing properties from the first filled in.

- Fields that already exist in the record should not be overwritten.

1. migrate_record({ "username": "", "posts": 0 }, { "verified": True }) should return { "username": "", "posts": 0, "verified": True }.
2. migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }) should return { "username": "camper", "posts": 5 }.
3. migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }) should return { "username": "camper", "posts": 0, "verified": False }.
4. migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }) should return { "username": "camper", "role": "admin", "posts": 0 }.
5. migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" })
    should return { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False }.
 */

function migrateRecord(schema, record) {
    for (const key in schema) {
        if (!(key in record)) {
            record[key] = schema[key];
        }
    }
    return record;
}


console.log(migrateRecord({ "username": "", "posts": 0 }, { "verified": true }));
console.log(migrateRecord({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }));
console.log(migrateRecord({ "username": "", "posts": 0, "verified": false }, { "username": "camper" }));
console.log(migrateRecord({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }));
console.log(migrateRecord({ "username": "", "email": "", "posts": 0, "verified": false, "role": "user", "banned": false },
    { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }));
