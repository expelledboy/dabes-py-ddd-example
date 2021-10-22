from enum import IntEnum
from typing import Union

from pydantic import EmailStr, confloat, conint, constr

from dabes_py_ddd_example.domain.abstract_model import AbstractModel
from dabes_py_ddd_example.domain.common.constraints import Regex
from dabes_py_ddd_example.domain.common.type_factory import (
    create_type,
    create_type_without_constructor,
)

String50 = create_type("String50", constr(max_length=50))

EmailAddress = create_type("EmailAddress", EmailStr)


class VipStatus(IntEnum):
    Normal = 1
    Vip = 2


ZipCode = create_type(
    "ZipCode", constr(min_length=5, max_length=10, regex=Regex.ZIP_CODE.value)
)

UsStateCode = create_type("UsStateCode", constr(max_length=2))

OrderId = create_type("OrderId", constr(max_length=50, regex=Regex.ORDER_ID.value))

ProductCode = create_type_without_constructor("ProductCode", str)

WidgetCode = create_type(
    "WidgetCode", constr(min_length=3, max_length=5), base_type=ProductCode
)

GizmoCode = create_type("GizmoCode", constr(min_length=6), base_type=ProductCode)

ProductCodeFactoryArg = Union[WidgetCode, GizmoCode]

OrderQuantity = create_type_without_constructor("OrderQuantity", int)

UnitQuantity = create_type("UnitQuantity", conint(gt=0, le=1000))

KilogramQuantity = create_type("KilogramQuantity", confloat(gt=0.05, le=100))

OrderQuantityFactoryArg = Union[UnitQuantity, KilogramQuantity]

Price = create_type("Price", conint(gt=0, le=1000))

BillingAmount = create_type("BillingAmount", confloat(gt=0, le=10000))


class PdfAttachment(AbstractModel):
    name: String50
    bytes: bytes


PromotionCode = create_type(
    "PromotionCode", constr(min_length=6, max_length=20, regex=Regex.PROMO_CODE.value)
)
