"""
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
"""

def extract_attributes(element: str) -> list[str]:
    # Variables for attribute indicators, flags and indices.
    attr_indicator_0 = ' '
    attr_indicator_1 = '='
    attr_indicator_2 = '"'
    attr_flag_0 = False
    attr_flag_1 = False
    attr_flag_2 = False
    attr_index_0 = 0
    attr_index_2 = 0

    # Lists for each step of extraction process. 'extracted_attributes' for return.
    extracted_elements = []
    extracted_attributes = []

    for index, char in enumerate(element):
        # Check for first indicator.
        if char == attr_indicator_0 and not attr_flag_1:
            attr_flag_0 = True
            attr_index_0 = index
        # Check for second indicator.
        elif char == attr_indicator_1:
            attr_flag_1 = True
        # Check for third indicator. Ensuring it's the second '"' by checking if it is preceded by '='.
        elif char == attr_indicator_2 and element[index-1] != attr_indicator_1:
            attr_flag_2 = True
            attr_index_2 = index

        # Add extracted attribute elements to list 'extracted_elements' if all indicators have been found.
        if attr_flag_0 and attr_flag_1 and attr_flag_2:
            extracted_elements.append(element[attr_index_0:attr_index_2].lstrip().rstrip())
            attr_flag_0 = False
            attr_flag_1 = False
            attr_flag_2 = False
            attr_index_0 = 0
            attr_index_2 = 0

    for item in extracted_elements:
        key, value = item.split('="')
        extracted_attributes.append(f"{key}, {value}")

    return extracted_attributes


print(extract_attributes('<span class="red"></span>'))
print(extract_attributes('<meta charset="UTF-8" />'))
print(extract_attributes("<p>Lorem ipsum dolor sit amet</p>"))
print(extract_attributes('<input name="email" type="email" required="true" />'))
print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))
