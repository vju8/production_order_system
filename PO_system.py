from product import FinalProduct, ProductionProcess, Component
import time
from tqdm import tqdm


class ProductionOrder:
   def __init__(self, order_number, final_product_amount):
      self.order_number = order_number
      self.final_product_amount = final_product_amount
      self.next = None

   def __str__(self):
      return str(self.order_number)

   def calculate_total_PO_production_time(self, product_production_time): 
      return product_production_time * self.final_product_amount

   def calculate_total_PO_cost(self, final_product_cost, margin = 35):
      return final_product_cost * self.final_product_amount * (margin/100 + 1)


class ProductionQueue:
   def __init__(self):
      self.front = None
      self.rear = None

   def __iter__(self): 
      currPO = self.front
      while currPO:
         yield currPO.order_number
         currPO = currPO.next

   def __str__(self):
      print("\nThe PO Queue:")
      result = ""
      currPO = self.front
      while currPO:
         result += currPO.order_number
         if currPO.next:
            result += " -> "
         currPO = currPO.next
      return result

   def __len__(self): 
      counter = 0
      currPO = self.front
      while currPO: 
         counter += 1
         currPO = currPO.next 
      return counter 
   
   def enqueue(self, order_number, final_product_amount):
      new_order = ProductionOrder(order_number, final_product_amount)
      if self.isEmpty():
         self.front = new_order
         self.rear = new_order
      else:
         self.rear.next = new_order
         self.rear = new_order
      return f"New order '{new_order}' added."
   
   def dequeue(self):
      if self.isEmpty():
         return None
      temp = self.front
      self.front = self.front.next
      if self.front is None:
         self.rear = None
      return temp

   def isEmpty(self):
      if not self.front:
         return True
      else:
         return False


# Testing the production order system
if __name__ == "__main__":
   
   def establish_factory():
      # Establishment of Production Logics
      # Instantiate Components:
      product1 = Component("Outer Spring", 50)
      product2 = Component("Inner Spring", 25)
      product3 = Component("Damper", 60)
      product4 = Component("Casing", 15)

      # Instantiate Production Processes:
      production_process1 = ProductionProcess("Outer Spring Manufacturing", 2, 100.00, [product1])
      production_process2 = ProductionProcess("Inner Spring Manufacturing", 1, 70.00, [product1])
      production_process3 = ProductionProcess("Damper Manufacturing", 3, 120.00, [product3])
      production_process4 = ProductionProcess("Casing Manufacturing", 1, 65.00, [product4])
      production_process5 = ProductionProcess("Final Assembly", 3, 80.00, [product1, product2, product3, product4])

      # Instantiate Final Product
      final_product = FinalProduct("Spring-Damper Unit",
                                 {product1 : 1, 
                                 product2 : 3, 
                                 product3 : 1, 
                                 product4 : 1}, 
                                 [production_process1, production_process2, production_process2, production_process2, production_process3, production_process4, production_process5])
      
      return final_product


   def place_orders():
         production_queue = ProductionQueue()
         
         # Placing orders (enqueue)
         production_queue.enqueue("PO1000", 2)
         production_queue.enqueue("PO1001", 1)
         production_queue.enqueue("PO1002", 3)
         production_queue.enqueue("PO1003", 2)

         return production_queue


   def process_orders(production_queue, final_product):
      # Processing orders (dequeue)
      print("\n\tOrder Processing starts.")
      for order in (range(len(production_queue))):
         PO_to_produce = production_queue.dequeue()
         print(f"\nNow the PO '{PO_to_produce}' is being produced:")
         for i in tqdm(range(PO_to_produce.calculate_total_PO_production_time(final_product.calculate_product_production_time())), desc='PO Processing', ncols = 100):
            time.sleep(1)
         print(f"PO '{PO_to_produce}' production finished. PO Revenue = ${PO_to_produce.calculate_total_PO_cost(final_product.calculate_production_costs())}:")
      print("\n\tOrder Processing finished.")

   
   final_product = establish_factory()
   final_product.display_BOM()
   final_product.display_production_flow()
   production_queue = place_orders()
   print(production_queue)
   process_orders(production_queue, final_product)

   

