from contextlib import contextmanager
from typing import ContextManager

from attr import dataclass
from dabes_py_ddd_example.domain.common.types import (
    EmailAddress,
    GizmoCode,
    ProductCode,
    String50,
    WidgetCode,
)
from pydantic import ValidationError
from pytest import mark, raises


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
def test_validation(type_, test_value, expectation: ContextManager):
    with expectation:
        assert type_(test_value) == test_value


@mark.parametrize(
    ["type_", "value", "expectation"],
    [
        (WidgetCode, "abc1", does_not_raise()),
        (GizmoCode, "abcd1234", does_not_raise()),
        (EmailAddress, "example@example.com", raises(ValidationError)),
    ],
)
def test_union_type(type_, value, expectation: ContextManager):
    with expectation:
        product_code = ProductCode(type_(value))
        assert isinstance(product_code, type_)
