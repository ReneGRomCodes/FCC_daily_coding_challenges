"""
URL Query Parser
Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

- The query string begins after the "?",
- each parameter is separated by "&",
- each key/value pair is separated by "="

For example, given "https://example.com/search?name=Alice&age=30", return:
{
  "name": "Alice",
  "age": "30"
}

All values should be returned as strings.

1. parse_url_query("https://example.com/search?name=Alice&age=30") should return {"name": "Alice", "age": "30"}
2. parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python")
        should return {"skill": "programming", "language": "python"}
3. parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2")
    should return {"category": "books", "sort": "asc", "page": "2"}
4. parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now")
    should return {"redirect": "freecodecamp.org/learn", "when": "now"}
"""


def parse_url_query(url: str) -> dict[str, str]:
    queries: list[str] = url[url.index("?") + 1:].split("&")
    queries_dict: dict[str, str] = {}

    for query in queries:
        key_value: list[str] = query.split("=")
        queries_dict[key_value[0]] = key_value[1]

    return queries_dict


print(parse_url_query("https://example.com/search?name=Alice&age=30"))
print(parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python"))
print(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"))
print(parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now"))
