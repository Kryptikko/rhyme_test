from collections import Counter
from entities.Order import Order
from entities.Beverage import Beverage, UNALLOCATED

def setup_orders(orders):
    return map(Order, orders)

def _allocate_order_item_generator(machine):
    def allocate_order_item(item):
        for key in item:
            if key in machine:
                resource = machine[key] - item[key]
                if resource < 0:
                    # not enough of this resource to handle the order
                    return UNALLOCATED
                machine[key] = resource
        return machine.id

    return allocate_order_item


def _compose_beverage(item, item_spec):
    # add the base beverage
    beverage_spec = [item_spec[item.item]]
    # add the beverage addons
    for addon in item.add:
        beverage_spec.append(item_spec[addon])

    composite = sum(
        map(Counter, beverage_spec),
        Counter())

    composite['name'] = item.item
    # print beverage_spec
    # composite['name'] = "+".join(beverage_spec)
    return Beverage(composite)

def allocate_order(order, machines, beverage_spec):
    output = {
        "order": order,
        "allocated": [],
        "rejected": []
    }
    machine_pool = map(_allocate_order_item_generator, machines)

    for item in order.items:
        item.beverage = _compose_beverage(item, beverage_spec)
        for allocate_resource in machine_pool:
            item.beverage.allocated_machine = allocate_resource(item.beverage)
            if item.beverage.allocated_machine is not UNALLOCATED:
                output["allocated"].append(item)
                break

        if item.beverage.allocated_machine is UNALLOCATED:
            output["rejected"].append(item)

    return output

