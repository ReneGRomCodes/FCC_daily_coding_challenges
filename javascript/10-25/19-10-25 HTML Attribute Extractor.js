/*
HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format:
["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.

1. extract_attributes('<span class="red"></span>') should return ["class, red"].
2. extract_attributes('<meta charset="UTF-8" />') should return ["charset, UTF-8"].
3. extract_attributes("<p>Lorem ipsum dolor sit amet</p>") should return [].
4. extract_attributes('<input name="email" type="email" required="true" />') should return
    ["name, email", "type, email", "required, true"].
5. extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') should return
    ["id, submit", "class, btn btn-primary"].
 */

function extractAttributes(element) {
    // Variables for attribute indicators, flags and indices.
    const attrIndicator0 = ' ';
    const attrIndicator1 = '=';
    const attrIndicator2 = '"';
    let attrFlag0 = false;
    let attrFlag1 = false;
    let attrFlag2 = false;
    let attrIndex0 = 0;
    let attrIndex2 = 0;

    // Arrays for each step of extraction process. 'extractedAttributes' for return.
    const extractedElements = [];
    const extractedAttributes = [];

    for (let i = 0; i < element.length; i++) {
        const char = element[i];

        // Check for first indicator.
        if (char === attrIndicator0 && !attrFlag1) {
            attrFlag0 = true;
            attrIndex0 = i;
        // Check for second indicator.
        } else if (char === attrIndicator1) {
            attrFlag1 = true;
        // Check for third indicator. Ensuring it's the second '"' by checking if it is preceded by '='.
        } else if (char === attrIndicator2 && element[i-1] !== attrIndicator1) {
            attrFlag2 = true;
            attrIndex2 = i;
        }

        // Add extracted attribute elements to list 'extracted_elements' if all indicators have been found.
        if (attrFlag0 && attrFlag1 && attrFlag2) {
            extractedElements
                .push(element
                    .slice(attrIndex0, attrIndex2)
                    .trim());
            attrFlag0 = false;
            attrFlag1 = false;
            attrFlag2 = false;
            attrIndex0 = 0;
            attrIndex2 = 0;
        }
    }

    for (const item of extractedElements) {
        const [key, value] = item.split('="');
        extractedAttributes.push(`${key}, ${value}`)
    }

    return extractedAttributes;
}


console.log(extractAttributes('<span class="red"></span>'));
console.log(extractAttributes('<meta charset="UTF-8" />'));
console.log(extractAttributes("<p>Lorem ipsum dolor sit amet</p>"));
console.log(extractAttributes('<input name="email" type="email" required="true" />'));
console.log(extractAttributes('<button id="submit" class="btn btn-primary">Submit</button>'));
