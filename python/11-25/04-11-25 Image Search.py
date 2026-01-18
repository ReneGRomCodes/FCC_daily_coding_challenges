"""
Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this
challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.

1. image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") should return ["dog.png"].
2. image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") should return ["Sunset.jpg", "sunflower.jpeg"].
3. image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG") should return ["Moon.png", "stars.png"].
4. image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat")
    should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].
"""

def image_search(images: list[str], term: str) -> list[str] :
    return [x for x in images if term.lower() in x.lower()]


print(image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"))
print(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"))
print(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"))
print(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"))
