from products import Product
from store import Store

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def show_menu():
    print("""
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """)

def start(store:Store):
    while True:
        show_menu()
        user_input = input("Press choose a number")
        if user_input in ["1", "2", "3", "4"]:
            break

    for product in store.get_all_products():
        product.show()



def main():
    start(best_buy)


if __name__ == "__main__":
    main()
