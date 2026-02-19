import sys
from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)


def show_menu():
    """Show the main menu."""
    print("""
-----------------------------
‡         Store Menu        ‡
-----------------------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """)


def list_products(store: Store):
    """Print all products in the store."""
    print("-----------------------")
    for index, product in enumerate(store.get_all_products()):
        if product.active:
            print(index + 1, end=". ")
            product.show()
    print("-----------------------")


def show_total_amount_in_store(store: Store):
    """Show total quantity of all items."""
    total = store.get_total_quantity()
    print()
    print(f"Total of {total} items in store")


def get_order(store: Store):
    """Ask the user which products and quantities they want."""
    order = {}
    while True:
        print("When you want to finish order, enter empty text.")
        product_number = input("Which product # do you want? ").strip()
        product_quantity = input("What amount do you want? ").strip()

        if product_number == "" or product_quantity == "":
            break

        try:
            chosen_product = int(product_number)
            if chosen_product not in range(1, len(store.get_all_products()) + 1):
                print("product not found.")
                continue

            chosen_quantity = int(product_quantity)
        except ValueError:
            print("Please enter a valid number.")
            continue

        product_object = store.get_all_products()[chosen_product - 1]
        order[product_object] = order.get(product_object, 0) + chosen_quantity

    return order


def make_order(store: Store):
    """Handle the full order process."""
    list_products(store)
    user_order = get_order(store)
    total_amount = 0

    if not user_order:
        print("No order made!")
        return

    try:
        for product, quantity in user_order.items():
            price = product.buy(quantity)
            total_amount += price
    except Exception as error:
        print(error)
        return
    print(f"Order made! Total payment: ${total_amount}")


def start(store: Store):
    """Run the menu loop."""
    while True:
        show_menu()
        user_input = input("Press choose a number: ").strip()

        if user_input in ["1", "2", "3", "4"]:
            if user_input == "1":
                list_products(store)
            elif user_input == "2":
                show_total_amount_in_store(store)
            elif user_input == "3":
                make_order(store)
            else:
                sys.exit()


def main():
    """Start the program."""
    start(best_buy)


if __name__ == "__main__":
    main()
