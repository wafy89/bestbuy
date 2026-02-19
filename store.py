from products import Product


class Store:
    """A simple store that manages products."""

    def __init__(self, products: list[Product]) -> None:
        """Create a store with a list of products."""
        self.products = products

    def add_product(self, product: Product):
        """Add a product."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of all products."""
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self) -> list[Product]:
        """Return all products."""
        return self.products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Process an order and return total price."""
        total_price = 0.0

        for product, qty in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product '{product.name}' not found in store.")
            if qty > product.quantity:
                raise ValueError(
                    f"Not enough quantity for '{product.name}'. "
                    f"Requested: {qty}, Available: {product.quantity}"
                )

            product.quantity -= qty
            total_price += product.price * qty

        return total_price
