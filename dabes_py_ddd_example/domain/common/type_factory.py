from dabes_py_ddd_example.domain.common.errors import UnionError
from typing import Union

from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.errors import PydanticTypeError


def create_type(name: str, constraint: type, base_type: type = None) -> type:
    validator_class_namespace = {"__annotations__": {"value": constraint}}
    Validator = type(name, (BaseModel,), validator_class_namespace)

    def __init__(self, value):
        Validator(value=self)

    namespace = {"__init__": __init__}

    return type(name, (base_type or constraint,), namespace)


def create_union_type(name: str, *types) -> type:
    Validator = type(name, (BaseModel,), {})

    def __new__(self, value):
        if isinstance(value, tuple(types)):
            return value

        error_template_value = ", ".join((type_.__name__ for type_ in types)) 
        error = UnionError(types=error_template_value)
        raise ValidationError([ErrorWrapper(error, loc="value")], Validator)

    namespace = {"__new__": __new__}

    return type(name, (), namespace)
