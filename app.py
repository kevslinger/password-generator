import argparse
from flask import Flask, render_template, request
from waitress import serve
import random

app = Flask(__name__)


# TODO: formatting
NUMBER_CHARACTERS = [number for number in "1234567890"]
LOWERCASE_CHARACTERS = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
UPPERCASE_CHARACTERS = [letter.upper() for letter in LOWERCASE_CHARACTERS]
SYMBOL_CHARACTERS = [symbol for symbol in "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"]

# Home page
@app.route("/")
def landing():
    return render_template(
        "index.html",
        default_length=DEFAULT_LENGTH,
        default_numbers=DEFAULT_NUMBERS,
        default_lowercase=DEFAULT_LOWERCASE,
        default_uppercase=DEFAULT_UPPERCASE,
        default_symbols=DEFAULT_SYMBOLS,
    )


@app.route("/generate")
def generate():
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
            default_symbols=symbols,
        )
    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--default-length",
        type=int,
        default=10,
        help="Set the default generated password length.",
    )
    parser.add_argument(
        "--disable-lowercase",
        action="store_false",
        help="Use this to set the default for including lowercase letters in the randomly generated password to False.",
    )
    parser.add_argument(
        "--disable-uppercase",
        action="store_false",
        help="Use this to set the default for including uppercase letters in the randomly generated password to False.",
    )
    parser.add_argument(
        "--disable-numbers",
        action="store_false",
        help="Use this to set the default for including numbers in the randomly generated password to False.",
    )
    parser.add_argument(
        "--disable-symbols",
        action="store_false",
        help="Use this to set the default for including symbols in the randomly generated password to False.",
    )
    args = parser.parse_args()

    DEFAULT_LENGTH = args.default_length
    DEFAULT_LOWERCASE = args.disable_lowercase
    DEFAULT_UPPERCASE = args.disable_uppercase
    DEFAULT_NUMBERS = args.disable_numbers
    DEFAULT_SYMBOLS = args.disable_symbols
    serve(app, host="0.0.0.0", port=8080)
