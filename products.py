class Product:
    """A simple product with name, price, and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        """Create a product."""
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

    def get_quantity(self) -> int:
        """Return quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set quantity."""
        self.quantity = quantity

    def is_active(self) -> bool:
        """Return active status."""
        return self.active

    def activate(self):
        """Activate product."""
        self.active = True

    def deactivate(self):
        """Deactivate product."""
        self.active = False

    def show(self):
        """Print product info."""
        print(f"{self.name}, price: {self.price}, quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy a quantity and return total price."""
        if self.quantity < quantity:
            raise Exception("Not enough Quantity")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity
