def basic_validation(value):
    """
    Basic validation to check if the value is not None or empty.
    
    Args:
        value (str): The value to be checked.
    
    Returns:
        bool: True if the value is valid (not None or empty), False otherwise.
    """
    return value is not None and value != ""

def range_check(value, min_value, max_value):
    """
    Range check to ensure the value is within a specified range.
    
    Args:
        value (int): The value to be checked.
        min_value (int): The minimum acceptable value.
        max_value (int): The maximum acceptable value.
    
    Returns:
        bool: True if the value is within the range, False otherwise.
    """
    return min_value <= value <= max_value

def length_check(value, min_length, max_length):
    """
    Length check to ensure the value's length is within a specified range.
    
    Args:
        value (str): The value to be checked.
        min_length (int): The minimum acceptable length.
        max_length (int): The maximum acceptable length.
    
    Returns:
        bool: True if the value's length is within the range, False otherwise.
    """
    return min_length <= len(value) <= max_length

def presence_check(value):
    """
    Presence check to ensure the value is present (not None or empty).
    
    Args:
        value (str): The value to be checked.
    
    Returns:
        bool: True if the value is present, False otherwise.
    """
    return bool(value)

def type_check(value, expected_type):
    """
    Type check to ensure the value is of the expected type.
    
    Args:
        value: The value to be checked.
        expected_type (type): The expected type of the value.
    
    Returns:
        bool: True if the value is of the expected type, False otherwise.
    """
    return isinstance(value, expected_type)

def format_check(value, format_type):
    """
    Format check to ensure the value matches a specified format.
    
    Args:
        value (str): The value to be checked.
        format_type (str): The format type to check against ('date' or 'email').
    
    Returns:
        bool: True if the value matches the format, False otherwise.
    """
    if format_type == 'date':
        parts = value.split('-')
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            year, month, day = map(int, parts)
            return 1 <= month <= 12 and 1 <= day <= 31
    elif format_type == 'email':
        return '@' in value and '.' in value.split('@')[-1]
    return False

def check_digit(value):
    """
    Check digit validation to ensure the value ends with a valid check digit.
    
    Args:
        value (str): The value to be checked.
    
    Returns:
        bool: True if the check digit is valid, False otherwise.
    """
    if not value.isdigit():
        return False
    total = sum(int(digit) for digit in value[:-1])
    check_digit = total % 10
    return check_digit == int(value[-1])

def spelling_check(value, dictionary):
    """
    Spelling check to ensure the value is a correctly spelled word.
    
    Args:
        value (str): The value to be checked.
        dictionary (set): A set of correctly spelled words.
    
    Returns:
        bool: True if the value is correctly spelled, False otherwise.
    """
    return value in dictionary

# Example usage
if __name__ == "__main__":
    print(basic_validation("Hello"))  # True
    print(range_check(10, 1, 20))  # True
    print(length_check("Hello", 1, 10))  # True
    print(presence_check("World"))  # True
    print(type_check(123, int))  # True
    print(format_check("2024-10-18", 'date'))  # True
    print(format_check("example@example.com", 'email'))  # True
    print(check_digit("12345"))  # False
    print(spelling_check("hello", {"hello", "world"}))  # True
