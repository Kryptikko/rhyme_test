import argparse
import json
import sys
from src.config import config
from src.coffee_machines import init_machines, allocate_order
from src.orders import init_orders
from src.view import print_orders_summary, print_machine_summary, print_top_orders_summary

parser = argparse.ArgumentParser(description='Coffee Shop')

parser.add_argument('machine_count', metavar='machine_count', type=int,
                    help='number of coffee machines')
parser.add_argument('order', metavar='order_file', type=str,
                    help='order file (as JSON)')

args = parser.parse_args()

with open(args.order) as order_file:
    order_json = json.load(order_file)

# initialize workers
coffee_machines = init_machines(
    args.machine_count,
    config['coffee_machines_spec'])

# initialize orders as units of work
orders = init_orders(order_json,
    config['beverage_spec'])

for order in orders:
    order_allocation = allocate_order(order, coffee_machines)

print_orders_summary(orders)

print("\n=======\n")

print_top_orders_summary(orders)

print("\n=======\n")

print_machine_summary(orders)
