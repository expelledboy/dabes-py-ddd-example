from typing import Type, Union

from pydantic import ValidationError
from pydantic import constr, BaseModel


def create_type(name: str, constraint: type, base_type: type = None) -> type:

    temporary_class_namespace = {"__annotations__": {"value": constraint}}

    temporary_type = type(name, (BaseModel,), temporary_class_namespace)

    def __init__(self, *args):
        temporary_type(value=self)

    dict_ = {"__init__": __init__}

    return type(name, (base_type or constraint,), dict_)


WidgetCode = create_type("WidgetCode", constr(max_length=3))
GizmoCode = create_type("GizmoCode", constr(max_length=20))

ProductCodeValue = create_type("ProductCodeValue", Union[WidgetCode, GizmoCode], str)


class ProductCode(ProductCodeValue):
    @property
    def type(self) -> Type[Union[WidgetCode, GizmoCode]]:
        for class_ in [WidgetCode, GizmoCode]:
            try:
                class_(self)
                return class_
            except ValidationError:
                pass


class OrderQuantity:
    amount: int
    dimension: Union[Kg, Scalar]


class OrderDestination:
    gps: GPS = None
    address: Address = None

    @validate("root")
    def validate_all(cls, values: dict):
        ...


product_code = ProductCode(GizmoCode("123"))


print(type(product_code), product_code)
print(product_code.type)

# business talk
# WidgetCode = Type(base_model=str, max_length=10)
# WidgetCode = Type(str, MaxLength(10))

# print(type(product_code), product_code)


# from typing import NewType
# _Url = NewType('_Url', str)
# class URL:
#     def create(self, url: str) -> _Url:
#         if not s.startswith('https://'):
#             raise AssertionError(s)
#         return _Url(s)
# print(type(URL.create('https://example.com')) is str)  # prints `True`
