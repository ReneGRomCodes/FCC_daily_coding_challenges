/*
HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".

1. strip_tags('<a href="#">Click here</a>') should return "Click here".
2. strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
3. strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
4. strip_tags('<main id="main"><section class="section">section</section>
               <section class="section">section</section></main>') should return sectionsection.
 */

function stripTags(html) {
    const startTagChar = "<";
    const endTagChar = ">";
    let tagFlag = false;
    const strippedHtml = [];

    for (let i = 0; i < html.length; i++) {
        // Set flag if current character is part of a tag.
        if (html[i] === startTagChar) { tagFlag = true }
        else if (html[i] === endTagChar) { tagFlag = false }
        if (!tagFlag && html[i] !== endTagChar) { strippedHtml.push(html[i]) }
    }

    return strippedHtml.join("");
}


console.log(stripTags('<a href="#">Click here</a>'));
console.log(stripTags('<p class="center">Hello <b>World</b>!</p>'));
console.log(stripTags('<img src="cat.jpg" alt="Cat">'));
console.log(stripTags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'));
