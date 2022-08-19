from flask import Flask, render_template, request
from typing import Optional
import random

app = Flask(__name__)

DEFAULT_LENGTH = 10
DEFAULT_NUMBERS = True
DEFAULT_LOWERCASE = True
DEFAULT_UPPERCASE = True
DEFAULT_SYMBOLS = False

# TODO: formatting
NUMBER_CHARACTERS = [number for number in "1234567890"]
LOWERCASE_CHARACTERS = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
UPPERCASE_CHARACTERS = [letter.upper() for letter in LOWERCASE_CHARACTERS]
SYMBOL_CHARACTERS = [symbol for symbol in "!@#$%^&*()_-+=/:;<>,.?'\"][}{"]

# Home page
@app.route("/")
def landing():
    return render_template("index.html", default_length=DEFAULT_LENGTH, default_numbers=DEFAULT_NUMBERS, default_lowercase=DEFAULT_LOWERCASE, default_uppercase=DEFAULT_UPPERCASE, default_symbols=DEFAULT_SYMBOLS)


@app.route("/generate")
def generate(
):
    if request.method == "GET":
        length = int(request.args.get("length"))
        numbers = request.args.get("numbers")
        lowercase = request.args.get("lowercase")
        uppercase = request.args.get("uppercase")
        symbols = request.args.get("symbols")
        if not numbers and not lowercase and not uppercase and not symbols:
            # TODO: Format a proper error message
            raise ValueError("At least one of the options must be selected")
        possible_characters = []
        if numbers:
            possible_characters += NUMBER_CHARACTERS
        if lowercase:
            possible_characters += LOWERCASE_CHARACTERS
        if uppercase:
            possible_characters += UPPERCASE_CHARACTERS
        if symbols:
            possible_characters += SYMBOL_CHARACTERS
        print(f"Length: {length}")
        print(f"Numbers: {numbers}")
        print(f"Lowercase: {lowercase}")
        print(f"Uppercase: {uppercase}")
        print(f"Symbols: {symbols}")
        return render_template(
            "index.html",
            password="".join(
                [
                    possible_characters[random.randint(0, len(possible_characters) - 1)]
                    for _ in range(length)
                ]
            ),
            default_length=length,
            default_numbers=numbers,
            default_lowercase=lowercase,
            default_uppercase=uppercase,
            default_symbols=symbols
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


"""
Create a REST API that will generate passwords on demand
Subject to the following configurations
    Password Length
    Numbers flag (whether or not numbers are allowed in the password)
    Lowercase chars flag (whether or not lowercase ascii characters are allowed)
    Uppercase chars flag (whether or not lowercase ascii characters are allowed)
    Special symbols flag (whether or not special symbols are allowed, like %$@)

- Default password length and default flags are configurable from the server
- Max Length: 200 characters
- Raise an exception and return formatted response correspondibly in case a user makes a request with disabling all features
- Cover all edge cases


Layout:

Title
Generated Password
Password Length: Slider? Dropdown? Type?
Checkboxes for Flags (Numbers/Lowercase/Uppercase/Symbols)


"""
