/*
IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated
by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed.

1. is_valid_ipv4("192.168.1.1") should return True.
2. is_valid_ipv4("0.0.0.0") should return True.
3. is_valid_ipv4("255.01.50.111") should return False.
4. is_valid_ipv4("255.00.50.111") should return False.
5. is_valid_ipv4("256.101.50.115") should return False.
6. is_valid_ipv4("192.168.101.") should return False.
7. is_valid_ipv4("192168145213") should return False.
 */

function isValidIPv4(ipv4) {
    const octets = ipv4.split(".");

    if (octets.length !== 4) {
        return false;
    }

    for (const item of octets) {
        if (!/^\d+$/.test(item)) {
            return false;
        }

        const itemInt = Number(item);

        if (itemInt < 0 || itemInt > 255) {
            return false;
        }

        if (item.length > 1 && item[0] === "0") {
            return false;
        }
    }

    return true;
}


console.log(isValidIPv4("192.168.1.1"));
console.log(isValidIPv4("0.0.0.0"));
console.log(isValidIPv4("255.01.50.111"));
console.log(isValidIPv4("255.00.50.111"));
console.log(isValidIPv4("256.101.50.115"));
console.log(isValidIPv4("192.168.101."));
console.log(isValidIPv4("192168145213"));
