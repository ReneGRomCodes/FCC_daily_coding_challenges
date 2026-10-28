"""
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
"""

def sort(emails: list[str]) -> list[str]:
    mapped_emails: dict[str, str] = {}  # Dict for mapping of each address to lowercase version.
    domain_alpha: set[str] = set()  # Unique domains to be turned into sorted list further down.
    address_dict: dict[str, list [str]] = {}  # Dict with lists of usernames for each unique domain.
    output_lookup: list[str] = []  # Sorted list for lowercase versions of addresses.
    sorted_emails: list[str] = []  # List for final output.

    for address in emails:
        domain: str = address.split("@")[1].lower()
        username: str = address.split("@")[0].lower()

        mapped_emails[address.lower()] = address
        domain_alpha.add(domain)

        if domain not in address_dict:
            address_dict[domain] = [username]
        else:
            address_dict[domain].append(username)

    # Sort username and domain collections alphabetically.
    for domain in address_dict:
        address_dict[domain].sort()
    domain_alpha: list[str] = sorted(list(domain_alpha))

    for domain in domain_alpha:
        for username in address_dict[domain]:
            output_lookup.append(f"{username}@{domain}")

    for address in output_lookup:
        sorted_emails.append(mapped_emails[address])

    return sorted_emails


print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))
print(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]))
print(sort(["user@z.com", "user@y.com", "user@x.com"]))
print(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]))
print(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]))
