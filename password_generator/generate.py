import random

NUMBER_CHARACTERS = list("1234567890")
LOWERCASE_CHARACTERS = list("abcdefghijklmnopqrstuvwxyz")
UPPERCASE_CHARACTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
SYMBOL_CHARACTERS = list("~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/")


def generate_password(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
) -> str:
    """Generates a password of length `length` allowing some combination of lowercase and uppercase ASCII characters, numbers, and symbols"""
    possible_characters = []
    if numbers:
        possible_characters += NUMBER_CHARACTERS
    if lowercase:
        possible_characters += LOWERCASE_CHARACTERS
    if uppercase:
        possible_characters += UPPERCASE_CHARACTERS
    if symbols:
        possible_characters += SYMBOL_CHARACTERS
    return "".join(
        [
            possible_characters[random.randint(0, len(possible_characters) - 1)]
            for _ in range(length)
        ]
    )
