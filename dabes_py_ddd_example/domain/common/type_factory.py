from pydantic import BaseModel


def create_type(name: str, constraint: type, base_type: type = None) -> type:
    validator_class_namespace = {"__annotations__": {"value": constraint}}
    Validator = type(name, (BaseModel,), validator_class_namespace)

    def __init__(self, *args):
        Validator(value=self)

    namespace = {"__init__": __init__}

    return type(name, (base_type or constraint,), namespace)
