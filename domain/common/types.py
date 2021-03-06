from pydantic import EmailStr
from enum import Enum


# Constrained to be 50 chars or less, not null
class String50(str):
    pass


class EmailAddress(String50):
    def __init__(self, value):
        EmailStr.validate(value)


class VipStatus(Enum):
    Normal = 1
    Vip = 2


class ZipCode(str):
    pass


class UsStateCode(str):
    pass


# An Id for Orders. Constrained to be a non-empty string < 10 chars
class OrderId(str):
    pass


class OrderLineId(str):
    pass


class WidgetCode(str):
    pass


class GizmoCode(str):
    pass


class ProductCode(Enum):
    widget: WidgetCode
    gizmo: GizmoCode


class UnitQuantity(int):
    pass


class KilogramQuantity(float):
    pass


class OrderQuantity(str):
    unit: UnitQuantity
    kilogram: KilogramQuantity


class Price(float):
    pass


class BillingAmount(float):
    pass


class BillingAmount(float):
    pass


class PdfAttachment():
    Name: String50
    Bytes: list(str)


class PromotionCode(str):
    pass
