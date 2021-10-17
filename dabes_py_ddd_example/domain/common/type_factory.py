from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorWrapper

from dabes_py_ddd_example.domain.common.errors import UnionError


def create_type(name: str, constraint: type, base_type: type = None) -> type:
    validator_class_namespace = {"__annotations__": {"value": constraint}}
    validator_class = type(name, (BaseModel,), validator_class_namespace)

    def __init__(self, value):
        validator_class(value=self)

    namespace = {"__init__": __init__}

    return type(name, (base_type or constraint,), namespace)


def create_union_type(name: str, *types) -> type:
    validator_class = type(name, (BaseModel,), {})

    def __new__(self, value):
        if isinstance(value, tuple(types)):
            return value

        error_template_value = ", ".join((type_.__name__ for type_ in types))
        error = UnionError(types=error_template_value)
        raise ValidationError([ErrorWrapper(error, loc="value")], validator_class)

    namespace = {"__new__": __new__}

    return type(name, (), namespace)
