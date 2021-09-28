from pydantic import PydanticTypeError


class UnionError(PydanticTypeError):
    msg_template = "value is none of {types}"