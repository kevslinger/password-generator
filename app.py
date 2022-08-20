import argparse
from flask import Flask, render_template, request
from waitress import serve
from password_generator import generate


app = Flask(__name__)


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


# Routes to this page after Generate Password is clicked
@app.route("/generate", methods=["GET"])
def generate_page():
    # Only accept GET requests
    if request.method == "GET":
        # Get data from the input form
        lowercase = request.args.get("lowercase")
        uppercase = request.args.get("uppercase")
        numbers = request.args.get("numbers")
        symbols = request.args.get("symbols")
        # Proper error formatting 
        error = ""
        password = ""
        try:
            # Ensure the length parameter is an integer
            length = int(request.args.get("length"))
        except ValueError:
            error = "Password length must be an integer"
            length = DEFAULT_LENGTH
        else:
            # Ensure length is within min/max range
            if not 1 <= length <= 200:
                error = "Password length must be between 1 and 200"
            # Ensure at least one of the character options is used
            elif not (lowercase or uppercase or numbers or symbols):
                error = "Invalid Configuration: Must have at least one checkbox checked."
            # All checks have passed, so we can generate a password with the given configuration
            else:
                password = generate.generate_password(
                    length, lowercase, uppercase, numbers, symbols
                )
        return render_template(
            "index.html",
            default_length=length,
            default_numbers=numbers,
            default_lowercase=lowercase,
            default_uppercase=uppercase,
            default_symbols=symbols,
            password=password,
            error=error,
        )
    # Return the default page if we are sent a request other than GET
    return render_template(
        "index.html",
        default_length=DEFAULT_LENGTH,
        default_numbers=DEFAULT_NUMBERS,
        default_lowercase=DEFAULT_LOWERCASE,
        default_uppercase=DEFAULT_UPPERCASE,
        default_symbols=DEFAULT_SYMBOLS,
    )


if __name__ == "__main__":
    # Create an argument parser to customise the default settings from the server.
    parser = argparse.ArgumentParser(
        description="A REST API to generate random passwords."
    )
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