from collections import Counter
from orders import is_successful_order
from entities.Beverage import UNALLOCATED
from config import config


def get_beverage_name(item):
    beverage_ingidient_names = [item.item]
    beverage_ingidient_names += item.add

    name = []
    ingidient_names = Counter(beverage_ingidient_names)
    for key, val in ingidient_names.most_common():
        if val > 1:
            name.append("{count}x{name}".format(count=val, name=key.capitalize()))
        else:
            name.append(key.capitalize())
    return " + ".join(name)

def print_orders_summary(orders):
    print ("\nServed:")
    for order in orders:
        if is_successful_order(order):
            print ("\n")
            print_order_summary(order)

    print ("\nUncompleted:")
    for order in orders:
        if not is_successful_order(order):
            print ("\n")
            print_order_summary(order)


def print_order_summary(order):
    order_duration = sum(map(lambda i: i.etc, order.beverages.values()), 0)
    print("Order: #%s (%ss)" % (str(order.order), str(order_duration)))
    for order_item in order.items:
        beverage = order.beverages[order_item.id]
        prefix = '+'
        if beverage.allocated_to_machine is UNALLOCATED:
            prefix = '-'
        name = get_beverage_name(order_item)
        print("%s %s (%ss)" % (prefix, name, str(beverage.etc)))


def print_top_orders_summary(orders):
    all_order_items = []
    for order in orders:
        all_order_items += list(map(lambda i: i.item, order.items))

    cnt = Counter(all_order_items)
    list_lenght = 4
    print("Most Served (top %s):" % list_lenght)
    for (key, value) in cnt.most_common()[:list_lenght]:
        print("%s : %s" % (key, value))


def _sum(base, item, keys):
    for key in keys:
        base[key] += item.get(key, 0)
    return base

def _print_attributes(dictionary):
    for key in dictionary:
        print("%s: %s" % (key.capitalize(), dictionary[key]))
    print("\n")


def print_machine_summary(orders):
    all_beverages = []
    resources = ['water', 'coffee', 'milk', 'etc']
    used = dict.fromkeys(resources, 0)
    needed = dict.fromkeys(resources, 0)
    for order in orders:
        for beverage in order.beverages.values():
            needed = _sum(needed, beverage, resources)
            if beverage.allocated_to_machine is not UNALLOCATED:
                used = _sum(used, beverage, resources)

    print("Used:")
    _print_attributes(used)
    print("Needed:")
    _print_attributes(needed)
