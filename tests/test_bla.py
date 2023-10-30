import pytest

import re

import re

def validate_input(input_str):
    pattern = r'^[,\s]*[a-zA-Z0-9]*([,\s]+[a-zA-Z0-9]+)*[,\s]*$'

    if re.match(pattern, input_str):
        return re.sub(r'[\s,]+', ' ', input_str).strip()
    else:
        raise ValueError("Locust tags input is not valid. It should contain only comma or space-separated values.")

def format_tags(tags_input):
    tags_input = validate_input(tags_input)
    formatted_tags = "[" + ", ".join(tags_input.split(', ')) + "]"
    print(formatted_tags)
    return formatted_tags




# Define test cases for format_tags using the output of validate_input
format_tags_test_cases = [
    ("apple banana cherry", '[apple, banana, cherry]'),
    ("apple,  banana, cherry", "[apple, banana, cherry]"),
    ("", "[]"),
    (" ", "[]"),
]

@pytest.mark.parametrize("tags_input, expected", format_tags_test_cases)
def test_format_tags(tags_input, expected):
    result = format_tags(validate_input(tags_input))
    





