from typing import ContextManager

from pydantic import ValidationError
from pytest import mark, raises

from dabes_py_ddd_example.domain.common.errors import ConstructorCallNotAllowedError
from dabes_py_ddd_example.domain.order_taking.types import (
    EmailAddress,
    PdfAttachment,
    String50,
    ProductCode,
)
from tests.utils import does_not_raise


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


def test_product_code_constructor_not_allowed():
    with raises(ConstructorCallNotAllowedError):
        ProductCode("abc123")


class TestPdfAttachment:
    def test_ok(self):
        attachment = PdfAttachment(name="Doc.pdf", bytes=b"abc")

        assert attachment
