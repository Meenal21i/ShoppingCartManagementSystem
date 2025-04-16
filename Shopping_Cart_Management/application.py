import sys
from config import DEFAULT_CART_LIMIT, VALID_MENU_CHOICES, EXIT_CHOICE, MENU_OPTIONS
from static.handlers import get_valid_input
from static.validator import is_valid_item_name, validate_int, validate_non_empty
from Cart_manager.inventory import Inventory
from Cart_manager.shopping_cart import ShoppingCart
from Cart_manager.checkout import CheckoutProcessor
from auth.authentication import Authenticator

class InventoryApp:
    def __init__(self):
        auth = Authenticator()
        self.username, self.password = auth.authenticate_user()
        cart_limit = get_valid_input(
            prompt="Enter cart limit: ",
            validator=validate_int, 
            retries=3
        )
        if cart_limit is None:
            print(f"Cart limit is now set to {DEFAULT_CART_LIMIT} by default.")
            cart_limit = DEFAULT_CART_LIMIT
        self.inventory = Inventory()
        self.cart = ShoppingCart(self.inventory, cart_limit)
        self.checkout = CheckoutProcessor(self.cart, self.password)

    def create_inventory(self):
        total = get_valid_input(
            prompt="Enter total items to add to inventory: ",
            validator=validate_int,
            retries=3
        )
        if total is None:
            print("Invalid inputs, Application closing...")
            sys.exit()
        for item_count in range(total):
            for attempt in range(3):
                item_name = get_valid_input(f"Enter item-{item_count + 1} name: ", validate_non_empty)
                if item_name and is_valid_item_name(item_name):
                    break
                else:
                    print("Please enter a valid item name consisting of only letters.")
            else:
                print("---Max invalid attempts for item name. Skipping this item.---")
                continue
            item_quantity = get_valid_input(
                f"Enter quantity for {item_name}: ",
                validator=validate_int,
                retries=3
            )
            if item_quantity is None:
                print("---Invalid quantity. Skipping this item.---")
                continue
            try:
                self.inventory.add_item(item_name, item_quantity)
            except ValueError as error_message:
                print(f"Error: {error_message}")

    def show_menu(self):
        print("\n--- Operations ---")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")
            
    def run(self):
        self.create_inventory()
        if not self.inventory.items:
            print("Inventory is empty currently and will be restocked soon. Exiting application.")
            return
        while True:
            self.show_menu()
            choice = get_valid_input("Choose an option (1-6): ", lambda val: validate_int(val, min_value=1, max_value=6))
            if choice is None:
                continue
            if choice not in VALID_MENU_CHOICES:
                print("Please enter a valid option between 1 and 6.")
                continue
            match choice:
                case 1:
                    self.inventory.print_items()
                case 2:
                    self.cart.add_item()
                case 3:
                    self.cart.remove_item()
                case 4:
                    self.cart.print_items()
                case 5:
                    self.checkout.checkout_process()
                case EXIT_CHOICE:
                    print("Thank you for using the Shopping Management!")
                    break

def run_app():
    try:
        InventoryApp().run()
    except KeyboardInterrupt:
        print("\nExiting application.")