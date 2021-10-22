from pydantic import PydanticTypeError


class ConstructorCallNotAllowedError(Exception):
    pass


class UnionError(PydanticTypeError):
    msg_template = "value is none of {types}"
