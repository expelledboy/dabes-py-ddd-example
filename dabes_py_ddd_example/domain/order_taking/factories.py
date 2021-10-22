from typing import Callable

from dabes_py_ddd_example.domain.common.type_factory import create_union_type_factory
from dabes_py_ddd_example.domain.order_taking.types import (
    ProductCode,
    WidgetCode,
    GizmoCode,
    ProductCodeFactoryArg,
    OrderQuantityFactoryArg,
    OrderQuantity,
    UnitQuantity,
    KilogramQuantity,
)

create_product_code: Callable[
    [ProductCodeFactoryArg], ProductCode
] = create_union_type_factory("ProductCode", WidgetCode, GizmoCode)


create_order_quantity: Callable[
    [OrderQuantityFactoryArg], OrderQuantity
] = create_union_type_factory("OrderQuantity", UnitQuantity, KilogramQuantity)
