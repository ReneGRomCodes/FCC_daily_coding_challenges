/*
Email Sorter
On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are
billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the
part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com",
"john@example.com", "jill@mail.com"].

1. sort(["jill@mail.com", "john@example.com", "jane@example.com"])
    should return ["jane@example.com", "john@example.com", "jill@mail.com"].
2. sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"])
    should return ["bob@mail.com", "carol@mail.com", "alice@zoo.com"].
3. sort(["user@z.com", "user@y.com", "user@x.com"]) should return ["user@x.com", "user@y.com", "user@z.com"].
4. sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) should return ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"].
5. sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"])
    should return ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"].
 */

function sort(emails) {
    const mappedEmails = {};  // Object for mapping of each address to lowercase version.
    let domainAlpha = new Set();  // Unique domains to be turned into sorted array further down.
    const addressObj = {};  // Object with arrays of usernames for each unique domain.
    const outputLookup = [];  // Sorted array for lowercase versions of addresses.
    const sortedEmails = [];  // array for final output.

    for (const address of emails) {
        const [domain, username] = [address.split("@")[1].toLowerCase(), address.split("@")[0].toLowerCase()];
        mappedEmails[address.toLowerCase()] = address;
        domainAlpha.add(domain);

        !(domain in addressObj) ? addressObj[domain] = [username] : addressObj[domain].push(username);
    }

    // Sort username and domain collections alphabetically.
    for (const domain in addressObj) { addressObj[domain].sort() }
    domainAlpha = [...domainAlpha].sort();

    for (const domain of domainAlpha) {
        for (const username of addressObj[domain]) { outputLookup.push(`${username}@${domain}`)}
    }

    for (const address of outputLookup) { sortedEmails.push(mappedEmails[address]) }

    return sortedEmails;
}


console.log(sort(["jill@mail.com", "john@example.com", "jane@example.com"]));
console.log(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]));
console.log(sort(["user@z.com", "user@y.com", "user@x.com"]));
console.log(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]));
console.log(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]));
