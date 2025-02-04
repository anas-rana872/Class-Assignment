import pandas as pd
import re


def clean_customer_params(text):
    """Replaces double backslashes with single backslashes in 'blr_customer_params'."""
    print(type(text))
    if pd.isna(text):  # Handle NaN values
        return text


#Define replacements using raw strings for proper escaping
    replacements = {
        r"\\d": r"\d",   # \d in regex matches digits
        r"\\D": r"\D",   # \D in regex matches non-digits
        r"\\w": r"\w",   # \w in regex matches word characters
        r"\\W": r"\W",   # \W in regex matches non-word characters
        r"\\s": r"\s",   # \s in regex matches whitespace
        r"\\S": r"\S"    # \S in regex matches non-whitespace
    }

    # Apply each pattern replacement
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)

    return text
