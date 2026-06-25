"""
Frontmatter Parser
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with
the keys and values.

Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:

---
title: My Post
draft: false
views: 100
---

Should return:
{
  title: "My Post",
  draft: false,
  views: 100
}

- Numbers, Booleans, and Strings should all be returned as their respective type.
- The given string will have new lines separated with the newline character ("\n"). The above example would be given as:
  "---\ntitle: My Post\ndraft: false\nviews: 100\n---".

1. parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")
    should return { title: "My Post", draft: False, views: 100 }.
2. parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---")
    should return { id: "6a174db57256a112f932195c", title: "My Book", locale: "en", wordCount: 10000, published: False }.
3. parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---")
    should return { version: "1.0.0", url: "https://example.com", private: True }.
4. parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---") should return { rating: 4.5, price: 9.99 }.
"""

def cast_value(v: str) -> str | bool | float:
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False

    if v.isdigit():
        return int(v)

    try:
        return float(v)
    except ValueError:
        pass

    return v


def parse_frontmatter(s: str) -> dict:
    cleaned_s: list[str] = s.lstrip("---\n").rstrip("\n---").split("\n")
    parsed_fm: dict = {}

    for item in cleaned_s:
        k, v = item.split(": ")
        parsed_fm[k] = cast_value(v)

    return parsed_fm


print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
print(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))
print(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))
print(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"))
