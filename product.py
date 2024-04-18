
class Component:
    def __init__(self, name, material_cost):
        self.name = name
        self.material_cost = material_cost

    def __str__(self):
        return str(self.name)


class ProductionProcess:
    def __init__(self, name, duration, operation_cost, products_required):
        self.name = name
        self.duration = duration
        self.operation_cost = operation_cost
        self.products_required = products_required


class FinalProduct:
    def __init__(self, name, products_and_amount, production_processes):
        self.name = name
        self.products = products_and_amount.keys()
        self.amounts = products_and_amount.values()
        self.production_processes = production_processes
        
    def display_BOM(self):
        print(f"\n'{self.name}' BOM:")
        for elem in zip(self.products, self.amounts):
            print(f"\t- Product: {elem[0].name} - Amount: {elem[1]} - Unit Price: ${elem[0].material_cost}")

    def display_production_flow(self):
        print(f"\n'{self.name}' Production Flow:")
        for step, process in enumerate(self.production_processes):
            print(f"\t{step+1}) {process.name} - {process.duration} min")

    def calculate_production_costs(self):
        tot_operation_cost = sum([operation.operation_cost for operation in self.production_processes])
        tot_material_costs = sum([elem[0].material_cost * elem[1] for elem in zip(self.products, self.amounts)])
        return sum([tot_operation_cost, tot_material_costs])

    def calculate_product_production_time(self):
        return sum([operation.duration for operation in self.production_processes])


