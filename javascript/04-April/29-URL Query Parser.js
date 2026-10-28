/*
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
 */

function parseUrlQuery(url) {
    const queries = url
        .slice(url.indexOf("?") + 1)
        .split("&");
    const queriesObj = {};

    for (const query of queries) {
        const keyValue = query.split("=");
        queriesObj[keyValue[0]] = keyValue[1];
    }

    return queriesObj;
}


console.log(parseUrlQuery("https://example.com/search?name=Alice&age=30"));
console.log(parseUrlQuery("https://freecodecamp.org/learn?skill=programming&language=python"));
console.log(parseUrlQuery("https://freecodecamp.org/items?category=books&sort=asc&page=2"));
console.log(parseUrlQuery("https://example.com?redirect=freecodecamp.org/learn&when=now"));
