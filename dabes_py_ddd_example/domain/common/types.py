from enum import Enum, IntEnum
from typing import Union

from dabes_py_ddd_example.domain.abstract_model import AbstractModel
from pydantic import EmailStr, confloat, conint, constr

from .constraints import Regex
from .type_factory import create_type

String50 = create_type("String50", constr(max_length=50))

EmailAddress = create_type("EmailAddress", EmailStr)


class VipStatus(IntEnum):
    Normal = 1
    Vip = 2


OrderId = create_type("OrderId", constr(max_length=5, regex=Regex.ZIP_CODE.value))

UsStateCode = create_type("UsStateCode", constr(max_length=2))

OrderId = create_type("OrderId", constr(max_length=10, regex=Regex.ORDER_ID.value))

WidgetCode = create_type("WidgetCode", constr(min_length=3, max_length=5))

GizmoCode = create_type("GizmoCode", constr(min_length=6))

ProductCode = Union[WidgetCode, GizmoCode]

UnitQuantity = conint()

KilogramQuantity = conint()

OrderQuantity = Union[UnitQuantity, KilogramQuantity]

Price = confloat()

BillingAmount = confloat()


class PdfAttachment(AbstractModel):
    Name: String50
    Bytes: list[str]


PromotionCode = constr(max_length=20, regex=Regex.PROMO_CODE.value)