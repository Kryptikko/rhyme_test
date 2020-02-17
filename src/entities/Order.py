from schematics.models import Model
from schematics.types import (
    IntType,
    UUIDType,
    StringType,
    ListType,
    DictType,
    ModelType,
    BooleanType)
from src.entities.Beverage import Beverage


class OrderItem(Model):
    id = StringType()
    item = StringType(required=True)
    add = ListType(StringType)

    def __repr__(self):
        return "<OrderItem(item='%s')>" % (self.item)


class Order(Model):
    order = IntType(required=True)
    items = ListType(ModelType(OrderItem), default=[])
    beverages = DictType(
            ModelType(Beverage),
            default=lambda: {},
            serialize_when_none=True,)

    def __repr__(self):
        return "<Order(order='%s')>" % (self.order)
