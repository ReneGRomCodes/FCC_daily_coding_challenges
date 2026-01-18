"""
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
"""

def strip_tags(html: str) -> str:
    start_tag_char: str = "<"
    end_tag_char: str = ">"
    tag_flag: bool = False

    stripped_html: str = ""

    for index, character in enumerate(html):
        # Set flag to 'True' if current character is part of a tag.
        if character == start_tag_char:
            tag_flag = True
        elif character == end_tag_char:
            tag_flag = False

        if not tag_flag and character != end_tag_char:
            stripped_html += character

    return stripped_html


print(strip_tags('<a href="#">Click here</a>'))
print(strip_tags('<p class="center">Hello <b>World</b>!</p>'))
print(strip_tags('<img src="cat.jpg" alt="Cat">'))
print(strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'))
