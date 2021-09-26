from enum import Enum


class Regex(Enum):
    USERNAME = r"^[a-z0-9-]{1,32}$"
    ORDER_ID = r"^[a-z0-9-]{1,10}$"
    PROMO_CODE = r"^[a-z0-9-]{1,20}$"
    ZIP_CODE = r"^[a-z0-9-]{1,6}$"
    EMAIL_ADDRESS = r"^.+@.+$"

    def __str__(self) -> str:
        return self.value


def create_string(field_name: str, constructor: callable, max_len: int, value: str):
    """
    Creates a string field with a maximum length.
    :param field_name: The name of the field.
    :param constructor: The constructor function.
    :param max_len: The maximum length of the string.
    :param value: The value of the field.
    :return: The constructed field.
    """

    # check if the value is not empty
    if value is None or value == "":
        raise ValueError(f"{field_name} cannot be empty.")

    # check if the value is not too long
    if len(value) > max_len:
        raise ValueError(f"{field_name} must be at most {max_len} characters long.")

    return constructor(value)
