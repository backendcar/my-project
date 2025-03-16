class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"product {self.name}")
        
    def __del__(self):
        print(f"product {self.name} deleted!")
        
product1 = Product("book", 1000, "good")
del product1
        
        