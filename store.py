from products import Product



class Store:
    def __init__(self, products:list[Product]) -> None:
        self.products = products

    def add_product(self,product:Product):
        self.products.append(product)

    def remove_product(self,product:Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self) -> list[Product]:
        return self.products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, qty in shopping_list:

            if product not in self.products:
                raise ValueError(f"Product '{product.name}' not found in store.")
            if qty > product.quantity:
                raise ValueError( f"Not enough quantity for '{product.name}'. " f"Requested: {qty}, Available: {product.quantity}" )

            product.quantity -= qty
            total_price += product.price * qty

        return total_price