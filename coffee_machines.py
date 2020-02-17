from entities.CoffeeMachine import CoffeeMachine
from entities.Beverage import UNALLOCATED

def init_machines(count, machine_spec):
    machines = []
    for i in range(count):
        machine_spec["id"] = i
        machine = CoffeeMachine(machine_spec)
        machine.validate()
        machines.append(machine)
    return machines

def _allocate_to_machine(beverage, machine):
    temp_machine_state = CoffeeMachine(machine)
    resources = ['water', 'coffee', 'milk']
    for resource in resources:
        remaining = machine[resource] - beverage[resource]
        temp_machine_state[resource] = remaining

    return temp_machine_state

def _machine_has_enough_resources(machine, beverage):
    resources = ['water', 'coffee', 'milk']
    for resource in resources:
        remaining = machine[resource] - beverage[resource]
        if remaining < 0:
            return False
    return True


def allocate_beverage_to_machines(beverage, machine_pool):
    for machine_id in range(len(machine_pool)):
        machine = machine_pool[machine_id]
        if _machine_has_enough_resources(machine, beverage):
            machine = _allocate_to_machine(beverage, machine)
            beverage.allocated_to_machine = machine.id
            machine_pool[machine_id] = machine
    return beverage


def allocate_order(order, machines):
    for beverage_id in order.beverages:
        beverage = allocate_beverage_to_machines(order.beverages[beverage_id], machines)
        order.beverages[beverage_id] = beverage
    return order
