from contextlib import contextmanager
from typing import ContextManager

from pydantic import ValidationError
from pytest import mark, raises

from dabes_py_ddd_example.domain.order_taking.types import (
    EmailAddress,
    GizmoCode,
    PdfAttachment,
    ProductCode,
    String50,
    WidgetCode,
)


@contextmanager
def does_not_raise():
    yield


@mark.parametrize(
    ["type_", "test_value", "expectation"],
    [
        (String50, "a" * 51, raises(ValidationError)),
        (String50, "a" * 50, does_not_raise()),
        (EmailAddress, "asd", raises(ValidationError)),
        (EmailAddress, "example@ecample.com", does_not_raise()),
    ],
)
def test_validation(type_: type, test_value, expectation: ContextManager):
    with expectation:
        assert type_(test_value) == test_value


@mark.parametrize(
    ["type_", "value", "expectation"],
    [
        (WidgetCode, "abc1", does_not_raise()),
        (GizmoCode, "abcd1234", does_not_raise()),
        (EmailAddress, "example@example.com", raises(ValidationError)),
    ],
    ids=["widget", "gizmo", "invalid"]
)
def test_union_type(type_: type, value, expectation: ContextManager):
    with expectation:
        product_code = ProductCode(type_(value))
        assert isinstance(product_code, type_)
        assert isinstance(product_code, ProductCode)


class TestPdfAttachment:
    def test_ok(self):
        attachement = PdfAttachment(
            name="Doc.pdf",
            bytes=b"abc"
        )

        assert attachement
