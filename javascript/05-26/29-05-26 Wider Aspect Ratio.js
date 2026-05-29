/*
Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height
ratio.

- The given strings will be in the format "WxH", for example, "1920x1080".
- The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces
  to "16:9".
- Return a string in format "W:H", for example, "16:9".

1. get_wider_aspect_ratio("1920x1080", "800x600") should return "16:9".
2. get_wider_aspect_ratio("1080x1350", "2048x1536") should return "4:3".
3. get_wider_aspect_ratio("640x480", "2440x1220") should return "2:1".
4. get_wider_aspect_ratio("360x640", "1080x1920") should return "9:16".
5. get_wider_aspect_ratio("3440x1440", "2048x858") should return "43:18".
6. get_wider_aspect_ratio("12345x61234", "12534x51234") should return "2089:8539".
 */


function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}


function getWidthHeight(w, h) {
    const divisor = gcd(w, h);
    return [w / divisor, h / divisor];
}

function getWiderAspectRatio(a, b) {
    const [aWidth, aHeight] = a.split('x').map(Number);
    const [bWidth, bHeight] = b.split('x').map(Number);

    let width, height;

    if (aWidth / aHeight > bWidth / bHeight) {
        [width, height] = getWidthHeight(aWidth, aHeight);
    } else {
        [width, height] = getWidthHeight(bWidth, bHeight);
    }

    return `${width}:${height}`;
}


console.log(getWiderAspectRatio("1920x1080", "800x600"));
console.log(getWiderAspectRatio("1080x1350", "2048x1536"));
console.log(getWiderAspectRatio("640x480", "2440x1220"));
console.log(getWiderAspectRatio("360x640", "1080x1920"));
console.log(getWiderAspectRatio("3440x1440", "2048x858"));
console.log(getWiderAspectRatio("12345x61234", "12534x51234"));
