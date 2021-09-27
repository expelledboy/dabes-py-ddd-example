from contextlib import contextmanager
from typing import ContextManager

from attr import dataclass
from dabes_py_ddd_example.domain.common.types import EmailAddress, String50
from pydantic import ValidationError
from pytest import mark, raises


@dataclass
class Scenario:
    type_: type
    test_value: any
    should_raise_error: bool


@mark.parametrize(
    "scenario",
    [
        Scenario(String50, "a" * 51, True),
        Scenario(String50, "a" * 50, False),
        Scenario(EmailAddress, "asd", True),
        Scenario(EmailAddress, "example@ecample.com", False),
    ],
)
def test_validation(scenario: Scenario):
    expectation = (
        raises(ValidationError) if scenario.should_raise_error else does_not_raise()
    )

    with expectation:
        assert scenario.type_(scenario.test_value) == scenario.test_value


@contextmanager
def does_not_raise():
    yield
