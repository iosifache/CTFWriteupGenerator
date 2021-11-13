#!/usr/bin/env python3
"""Script for generating CTF write-ups templates.

Usage:
    generate_writeup.py
"""

# Libraries
import re
import os
from enum import Enum
from urllib.parse import quote

from PyInquirer import prompt, print_json
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):
    """Class for validating stringified numbers."""
    def validate(self, document: Document) -> None:
        """Validates a stringified number.

        Args:
            document (Document): Document specific to prompt_toolkit

        Raises:
            ValidationError: The provided stringified numbers is invalid.
        """
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message="The provided stringified numbers is invalid.",
                cursor_position=len(document.text))


class DateValidator(Validator):
    """Class for validating stringified dates."""
    def validate(self, document: Document) -> None:
        """Validates a stringified date.

        Args:
            document (Document): Document specific to prompt_toolkit

        Raises:
            ValidationError: The provided stringified date is invalid.
        """
        pattern = re.compile(DATE_FORMAT)

        if not re.fullmatch(pattern, document.text):
            raise ValidationError(
                message="The provided stringified date is invalid.",
                cursor_position=len(document.text))


# Constants
DATE_FORMAT = r"^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$"
QUESTIONS = [{
    "type": "input",
    "name": "ctf_name",
    "message": "The name of the contest"
}, {
    "type": "input",
    "name": "challenge_name",
    "message": "The name of the challenge"
}, {
    "type": "input",
    "name": "contest_date",
    "message": "The date of the contest, in DD.MM.YYYY format",
    "validate": DateValidator
},
{
    "type": "input",
    "name": "flag",
    "message": "The flag"
}, {
    "type": "confirm",
    "name": "solve",
    "message": "Was the challenge solved during the contest?"
}, {
    "type":
    "checkbox",
    "name":
    "categories",
    "message":
    "The categories of the challenge",
    "choices": [{
        "name": "Cryptography"
    }, {
        "name": "Exploit"
    }, {
        "name": "Forensics"
    }, {
        "name": "Miscellaneous"
    }, {
        "name": "Mobile"
    }, {
        "name": "Penetration Testing"
    }, {
        "name": "Programming"
    }, {
        "name": "pwn"
    }, {
        "name": "Reverse Engineering"
    }, {
        "name": "Steganography"
    }, {
        "name": "Warm-up"
    }, {
        "name": "Web"
    }]
}, {
    "type": "input",
    "name": "score",
    "message": "The points offered after solving the challenge",
    "validate": NumberValidator
}, {
    "type": "confirm",
    "name": "files_attached",
    "message": "Were files attached to the challenge description?"
}, {
    "type": "confirm",
    "name": "alternative_solutions",
    "message": "Does the challenge has an alternative solutions?"
}]
BADGE_FORMAT = "![{}: {}](https://img.shields.io/badge/{}-{}-{}.svg)"
TITLE_FORMAT = "# {}: {}"
FIRST_DOCUMENT_PART = """
## Description

> Lorem ipsum
"""
ATTACHED_FILES_PART = """
## Attached Files

- Lorem ipsum
"""
SECOND_DOCUMENT_PART = """## Summary

Lorem ipsum

## Flag

```
{}
```

## Detailed Solution

Lorem ipsum"""
ALTERNATIVE_SOLUTIONS_PART = """
## Alternative Solutions

Lorem ipsum"""
FILENAME_FORMAT = "writeups/{}-{}.md"


class CustomDict(dict):
    """Dictionary class providing dot access to its members"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Color(Enum):
    """Enumeration defining a part of the colors allowed by shields.io"""
    GREEN = "brightgreen"
    RED = "red"
    BLUE = "blue"
    GRAY = "lightgrey"


class BashColor:
    """Enumeration defining colors used in bash printing"""
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"


def generate_badge(description: str, value: str, color: Color) -> str:
    """Generates a badge element.

    Args:
        description (str): Description of the attribute
        value (str): Value of the attribute
        color (Color): Color

    Returns:
        str: The generated badge element
    """
    url_description = quote(description)
    url_value = quote(value)

    return BADGE_FORMAT.format(description, value, url_description, url_value,
                               color.value)


def main():
    """Main function"""
    # Get user's detail
    answers = prompt(QUESTIONS)
    answers = CustomDict(answers)

    # Insert the title
    content = TITLE_FORMAT.format(answers.ctf_name, answers.challenge_name)
    content += 2 * '\n'

    # Insert the description badge
    content += generate_badge("Contest Date", answers.contest_date,
                              Color.GRAY) + "\n"
    content += generate_badge(
        "Solve Moment",
        "During The Contest" if answers.solve else "After The Contest",
        Color.GREEN if answers.solve else Color.RED) + "\n"
    for category in answers.categories:
        content += generate_badge("Category", category, Color.GRAY) + "\n"
    content += generate_badge("Score", answers.score, Color.GREEN) + "\n"

    # Insert the other parts of the content
    content += FIRST_DOCUMENT_PART + "\n"
    if answers.files_attached:
        content += ATTACHED_FILES_PART + "\n"
    content += SECOND_DOCUMENT_PART.format(answers.flag)
    if answers.alternative_solutions:
        content += "\n" + ALTERNATIVE_SOLUTIONS_PART

    # Generate the filename
    formatted_date = answers.contest_date.replace(".", "")
    formatted_challenge_name = "".join(
        filter(str.isalnum, answers.challenge_name))
    filename = FILENAME_FORMAT.format(formatted_date, formatted_challenge_name)

    # Write to the file
    with open(filename, "w") as file:
        file.write(content)

    # Print a success message
    print(BashColor.GREEN + BashColor.BOLD + '+' + BashColor.END +
          " The write-up file " + BashColor.BLUE + BashColor.BOLD + filename +
          BashColor.END + " was generated!")


if __name__ == "__main__":
    main()