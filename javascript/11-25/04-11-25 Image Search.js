/*
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
 */

function imageSearch(images, term) {

    return images;
}


console.log(imageSearch(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"));
console.log(imageSearch(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"));
console.log(imageSearch(["Moon.png", "sun.jpeg", "stars.png"], "PNG"));
console.log(imageSearch(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"));
