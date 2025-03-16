class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self,product_name,quantity):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
            
    def check_inventory(self):
        for product, quantity in self.products.items():
            print(f"{product}:{quantity} adad mojoud ast!")
        
inventory = Inventory()
inventory.add_product("Laptop", 10)
inventory.add_product("Phone", 6)
inventory.check_inventory()
