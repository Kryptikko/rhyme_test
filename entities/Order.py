from schematics.models import Model
from schematics.types import (
    IntType,
    StringType,
    ListType,
    ModelType,
    BooleanType)
from entities.Beverage import Beverage


class OrderItem(Model):
    item = StringType(required=True)
    add = ListType(StringType)
    beverage = ModelType(Beverage)

    def __repr__(self):
        return "<OrderItem(item='%s')>" % (self.item)


class Order(Model):
    order = IntType(required=True)
    items = ListType(ModelType(OrderItem), default=[])

    def __repr__(self):
        return "<Order(order='%s')>" % (self.order)
