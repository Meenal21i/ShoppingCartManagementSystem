import re
def validate_username(value: str) -> tuple[bool, str | None]:
    if value.isalnum() and 4 <= len(value) <= 10:
        return True, value
    return False, None

def validate_password(value: str) -> tuple[bool, str | None]:
    import re
    if not (4 <= len(value) <= 10):
        return False, "Invalid input"
    if re.search(r"[A-Za-z]", value) and re.search(r"\d", value):
        return True, value
    return False, "Invalid input"

def validate_non_empty(input_str):
    if input_str:
        return True, input_str
    return False, "Input cannot be empty."

def validate_int(input_str, min_value=1, max_value=None):
    """Validates if a string can be converted to int and within bounds."""
    try:
        value = int(input_str)
        if value < min_value:
            return False, f"Value must be >= {min_value}."
        if max_value is not None and value > max_value:
            return False, f"Value must be <= {max_value}."
        return True, value
    except ValueError:
        return False, "Invalid number format."
    
def is_valid_item_name(name):
    """Rejects name consisting number or symbol"""
    return bool(re.fullmatch(r'[A-Za-z]+', name.strip()))