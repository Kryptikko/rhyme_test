import uuid
from collections import Counter
from entities.Order import Order
from entities.Beverage import Beverage, UNALLOCATED


def init_orders(orders, beverage_spec={}):
    order_instance_set = []
    for order in orders:
        order_instance = Order(order)
        order_instance.validate()
        order_instance = _compute_beverages(order_instance, beverage_spec)
        order_instance_set.append(order_instance)

    return order_instance_set


def _compute_beverages(order, beverage_spec):
    for item in order.items:
        # alternatively make the id a compositve ot the order id and the order item id
        item_uuid = str(uuid.uuid4())
        item.id = item_uuid
        beverage = _compose_order_item_to_beverage(item, beverage_spec)
        order.beverages[item_uuid] = beverage
    return order


def _compose_order_item_to_beverage(item, bev_spec):
    beverage_spec = []
    # add the base beverage
    normalize_items = [item.item]
    # add the beverage addons
    normalize_items += item.add
    for order_item in normalize_items:
        if order_item not in bev_spec:
            raise Exception("Unsapported beverage: `%s`" % order_item)
        beverage_spec.append(bev_spec[order_item])

    composite = sum(
        map(Counter, beverage_spec),
        Counter())

    composite['order_item_id'] = item.id
    return Beverage(composite)


def is_successful_order(order):
    for beverage in order.beverages.values():
        if beverage.allocated_to_machine is UNALLOCATED:
            return False

    return True
