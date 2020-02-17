from schematics.models import Model
from schematics.types import IntType, StringType
from entities.Beverage import Beverage


class CoffeeMachine(Model):
    id = IntType(required=True)
    water = IntType(required=True)
    coffee = IntType(required=True)
    milk = IntType(required=True)

    def __repr__(self):
        return "<CoffeeMachine(id='%s')>" % (self.id)
