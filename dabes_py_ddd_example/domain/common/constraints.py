from enum import Enum


class Regex(Enum):
    USERNAME = r"^[a-z0-9-]{1,32}$"
    ORDER_ID = r"^[a-z0-9-]{1,10}$"
    PROMO_CODE = r"^[a-z0-9-]{1,20}$"
    ZIP_CODE = r"^[a-z0-9-]{1,6}$"
    EMAIL_ADDRESS = r"^.+@.+$"

    def __str__(self) -> str:
        return self.value
