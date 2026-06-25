/*
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
 */

function parseFrontmatter(str) {
    const lines = str.trim().replace(/^---|\n---$/g, '').split('\n');
    const parsedFm = {};

    for (const line of lines) {
        if (!line.includes(': ')) continue;

        const index = line.indexOf(': ');
        const key = line.slice(0, index);
        const valueStr = line.slice(index + 2);

        try {
            parsedFm[key] = JSON.parse(valueStr);
        } catch (e) {
            parsedFm[key] = valueStr;
        }
    }

    return parsedFm;
}


console.log(parseFrontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"));
console.log(parseFrontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"));
console.log(parseFrontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"));
console.log(parseFrontmatter("---\nrating: 4.5\nprice: 9.99\n---"));
