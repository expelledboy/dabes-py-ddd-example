
def create_string(field_name: str, constructor: function, max_len: int, value: str):
    """
    Creates a string field with a maximum length.
    :param field_name: The name of the field.
    :param constructor: The constructor function.
    :param max_len: The maximum length of the string.
    :param value: The value of the field.
    :return: The constructed field.
    """

    # check if the value is not empty
    if value is None or value == '':
        raise ValueError(f'{field_name} cannot be empty.')

    # check if the value is not too long
    if len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters long.")

    return constructor(value)