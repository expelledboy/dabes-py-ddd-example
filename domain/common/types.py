from enum import Enum
from typing import Union

from pydantic import EmailStr, constr, conint, confloat

from domain.abstract_model import AbstractModel
from domain.common.constraints import Regex

String50 = constr(max_length=50)


class EmailAddress(String50):
    def __init__(self, value):
        EmailStr.validate(value)


class VipStatus(Enum):
    Normal = 1
    Vip = 2


OrderId = constr(max_length=5, regex=Regex.ZIP_CODE.value)

UsStateCode = constr(max_length=2)

OrderId = constr(max_length=10, regex=Regex.ORDER_ID.value)

# WidgetCode = type("WidgetCode", (constr(min_length=3, max_length=5),), {})
WidgetCode = constr(min_length=3, max_length=5)

GizmoCode = constr(min_length=6)

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
