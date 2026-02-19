

class Product:

    def __init__(self, name:str, price:float,quantity:int):
        if quantity < 1:
            raise Exception("Not enough Quantity")
        if name == "":
            raise Exception("Product Name cannot be empty")
        if price <= 0:
            raise Exception("Product Price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self)->int:
        return self.quantity


    def set_quantity(self, quantity:int):
        self.quantity = quantity


    def is_active(self)->bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, price: {self.price}, quantity: {self.quantity}")


    def buy(self, quantity:int)-> float:
        if self.quantity < quantity:
            raise Exception("Not enough Quantity")
        self.quantity -= quantity
        return self.price * quantity