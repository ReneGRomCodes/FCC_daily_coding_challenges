/*
Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width
and height.

The input string is in the format "WxH". For example, "800x600".
The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format.

1. scale_image("800x600", 2) should return "1600x1200".
2. scale_image("100x100", 10) should return "1000x1000".
3. scale_image("1024x768", 0.5) should return "512x384".
4. scale_image("300x200", 1.5) should return "450x300".
 */

function scaleImage(size, scale) {
    const sizeList = size.split("x");

    return `${sizeList[0] * scale}x${sizeList[1] * scale}`;
}


console.log(scaleImage("800x600", 2));
console.log(scaleImage("100x100", 10));
console.log(scaleImage("1024x768", 0.5));
console.log(scaleImage("300x200", 1.5));
