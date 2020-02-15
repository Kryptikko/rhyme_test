from entities.CoffeeMachine import CoffeeMachine

def setup_machines(count, machine_spec):
    machines = []
    for i in range(count):
        machine_spec["id"] = i
        machine = CoffeeMachine(machine_spec)
        machine.validate()
        machines.append(machine)
    return machines


def execute_order(order_allocation):
    pass
