import argparse
import json
import sys
from config import config
from coffee_machines import setup_machines
from orders import setup_orders, allocate_order
from entities.Beverage import UNALLOCATED

parser = argparse.ArgumentParser(description='Coffee Shop')

parser.add_argument('machine_count', metavar='machine_count', type=int,
                    help='number of coffee machines')
parser.add_argument('order', metavar='order_file', type=str,
                    help='order file (as JSON)')

args = parser.parse_args()

with open(args.order) as order_file:
    order_json = json.load(order_file)

# TODO: handle validation
orders = setup_orders(order_json)

coffee_machines = setup_machines(
    args.machine_count,
    config['coffee_machines_spec'])


for order in orders:
    # allocate resources for orders
    # TODO: you should use a copy of coffee_machines
    # so that the modifications dont affect the global state
    order_allocation = allocate_order(order, coffee_machines, config['beverage_spec'])
    # execute work
    print "--- next order ---"
    # report work

all_beverages = sum(map(lambda order: map(lambda i: i.beverage, order.items), orders), [])


for order in orders:
    order_duration = sum(map(lambda i: i.beverage.etc, order.items), 0)
    print "Order: #%s (%ss)" % (str(order.order), str(order_duration))
    for order_item in order.items:
        prefix = '+'
        if order_item.beverage.allocated_machine is UNALLOCATED:
            prefix = '-'
        print "%s %s (%ss)" % (prefix, order_item.beverage.name.capitalize(), str(order_item.beverage.etc))
