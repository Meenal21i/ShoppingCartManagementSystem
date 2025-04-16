def read_input(prompt, allow_cancel=True):
    """Reads normal input and handles optional cancellation."""
    input_value = input(prompt).strip()
    if allow_cancel and input_value.lower() == 'cancel':
        return None
    return input_value

def get_valid_input(prompt, validator, retries=3, allow_cancel=True):
    """Handles retries and redirects validation."""
    for attempt in range(retries):
        input_str = read_input(prompt, allow_cancel)
        if input_str is None:
            return None
        valid, result = validator(input_str)
        if valid:
            return result
        if result:
            print(result)
        else:
            print("Invalid Input.")
    print("Max retries reached. Returning to main menu.")
    return None

def confirm_action(prompt):
    return input(prompt + " (yes/no): ").strip().lower() == 'yes'