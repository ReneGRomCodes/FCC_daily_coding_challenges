/*
Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.

1. get_extension("document.txt") should return "txt".
2. get_extension("README") should return "none".
3. get_extension("image.PNG") should return "PNG".
4. get_extension(".gitignore") should return "gitignore".
5. get_extension("archive.tar.gz") should return "gz".
6. get_extension("final.draft.") should return "none".
 */

function getExtension(filename) {
    if (!filename.includes(".")) {
        return "none";
    }

    const extension = filename.split(".").pop();
    return extension || "none";
}


console.log(getExtension("document.txt"));
console.log(getExtension("README"));
console.log(getExtension("image.PNG"));
console.log(getExtension(".gitignore"));
console.log(getExtension("archive.tar.gz"));
console.log(getExtension("final.draft."));
