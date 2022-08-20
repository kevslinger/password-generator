import pytest
from password_generator.generate import (
    generate_password,
    LOWERCASE_CHARACTERS,
    UPPERCASE_CHARACTERS,
    NUMBER_CHARACTERS,
    SYMBOL_CHARACTERS,
)


@pytest.mark.parametrize(
    "length,lowercase,uppercase,numbers,symbols",
    [
        (10, False, False, False, False),
        (2000, False, False, False, False),
    ],
)
def test_generate_password_fails(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
):
    with pytest.raises(ValueError):
        generate_password(length, lowercase, uppercase, numbers, symbols)


@pytest.mark.parametrize(
    "length,lowercase,uppercase,numbers,symbols", [(10, False, True, True, True), (200, False, True, True, True)]
)
def test_generate_password_without_lowercase(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
):
    """Test that generate does not include any lowercase letters when lowercase is False"""
    assert (
        len(
            set(LOWERCASE_CHARACTERS).intersection(
                set(generate_password(length, lowercase, uppercase, numbers, symbols))
            )
        )
        == 0
    )

@pytest.mark.parametrize(
    "length,lowercase,uppercase,numbers,symbols", [(10, True, False, True, True), (200, True, False, True, True)]
)
def test_generate_password_without_uppercase(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
):
    """Test that generate does not include any uppercase letters when uppercase is False"""
    assert (
        len(
            set(UPPERCASE_CHARACTERS).intersection(
                set(generate_password(length, lowercase, uppercase, numbers, symbols))
            )
        )
        == 0
    )

@pytest.mark.parametrize(
    "length,lowercase,uppercase,numbers,symbols", [(10, True, True, False, True), (200, True, True, False, True)]
)
def test_generate_password_without_numbers(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
):
    """Test that generate does not include any numbers when numbers is False"""
    assert (
        len(
            set(NUMBER_CHARACTERS).intersection(
                set(generate_password(length, lowercase, uppercase, numbers, symbols))
            )
        )
        == 0
    )

@pytest.mark.parametrize(
    "length,lowercase,uppercase,numbers,symbols", [(10, True, True, True, False), (200, True, True, True, False)]
)
def test_generate_password_without_symbols(
    length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool
):
    """Test that generate does not include any special symbols when symbols is False"""
    assert (
        len(
            set(SYMBOL_CHARACTERS).intersection(
                set(generate_password(length, lowercase, uppercase, numbers, symbols))
            )
        )
        == 0
    )
