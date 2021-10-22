from typing import ContextManager

from pydantic import ValidationError
from pytest import mark, raises

from dabes_py_ddd_example.domain.order_taking.factories import create_product_code
from dabes_py_ddd_example.domain.order_taking.types import (
    WidgetCode,
    GizmoCode,
    EmailAddress,
    ProductCode,
)
from tests.utils import does_not_raise


@mark.parametrize(
    ["type_", "not_type", "value", "expectation"],
    [
        (WidgetCode, GizmoCode, "abc1", does_not_raise()),
        (GizmoCode, WidgetCode, "abcd1234", does_not_raise()),
        (EmailAddress, None, "example@example.com", raises(ValidationError)),
    ],
    ids=["widget", "gizmo", "invalid"],
)
def test_create_product_code(
    type_: type, not_type: type, value, expectation: ContextManager
):
    with expectation:
        product_code = create_product_code(type_(value))
        assert isinstance(product_code, type_)
        assert isinstance(product_code, ProductCode)
        assert not isinstance(product_code, not_type)
