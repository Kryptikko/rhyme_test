from schematics.models import Model
from schematics.types import IntType, StringType, FloatType

UNALLOCATED = -1


class Beverage(Model):
    """
        A Beverage is the unit of work for a coffee machine
    """
    order_item_id = StringType()
    water = IntType(default=0)
    coffee = IntType(default=0)
    milk = IntType(default=0)
    etc = FloatType(default=0)
    allocated_to_machine = IntType(default=UNALLOCATED)

    def __repr__(self):
        return "<Beverage(order_item_id='%s')>" % (self.order_item_id)
