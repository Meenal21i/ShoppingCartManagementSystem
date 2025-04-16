from config import MAX_QUANTITY_RETRIES
from static.handlers import read_input, get_valid_input, confirm_action
from static.validator import validate_int, validate_non_empty
from interfaces.removables import ItemRemover
from interfaces.addables import ItemAdder
from interfaces.printable import ItemPrinter

class ShoppingCart(ItemRemover, ItemAdder, ItemPrinter):
    def __init__(self, inventory, cart_limit):
        self.cart = {}
        self.inventory = inventory
        self.limit = cart_limit

    def _standard_item_name(self, item_name):
        return item_name.strip().lower()
    
    def clear_cart(self):
        self.cart.clear()

    def print_items(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            for item, qty in self.cart.items():
                print(f"{item.capitalize()}: {qty}")

    def _get_valid_quantity(self, prompt, max_allowed):
        return get_valid_input(
            prompt=prompt,
            validator=lambda val: validate_int(val, min_value=1, max_value=max_allowed),
            retries=MAX_QUANTITY_RETRIES,
            allow_cancel=True
        )
    
    def add_item(self):
        self.inventory.print_items()
        item_to_be_added = read_input("Enter item to add or 'cancel': ", validate_non_empty)
        if item_to_be_added is None:
            print("Operation cancelled.")
            return
        item_to_be_added = self._standard_item_name(item_to_be_added)
        if not self.inventory.if_item_exists(item_to_be_added):
            print("Item not found in inventory.")
            if confirm_action("Would you like to try adding another item?"):
                return self.add_item()
            print("Returning to menu.")
            return
        if self.inventory.current_quantity(item_to_be_added) == 0:
            print(f"{item_to_be_added.capitalize()} is out of stock!")
            return
        if len(self.cart) >= self.limit and item_to_be_added not in self.cart:
            print(f"Cart limit reached. Only {self.limit} unique items allowed.")
            return
        max_quantity = self.inventory.current_quantity(item_to_be_added)
        item_quantity = self._get_valid_quantity(
            f"Enter quantity of {item_to_be_added.capitalize()} to add (max {max_quantity}) or 'cancel': ",
            max_quantity
        )
        if item_quantity is None:
            print("Operation cancelled.")
            return
        self.cart[item_to_be_added] = self.cart.get(item_to_be_added, 0) + item_quantity
        self.inventory.reduce_item_quantity(item_to_be_added, item_quantity)
        print(f"Added {item_quantity} {item_to_be_added.capitalize()} to cart.")

    def remove_item(self):
        if not self.cart:
            print("Cart is empty. Cannot remove items.")
            return
        self.print_items()
        item_to_be_removed = read_input("Enter item to remove or 'cancel': ", validate_non_empty)
        if item_to_be_removed is None:
            print("Operation cancelled.")
            return
        item_to_be_removed = self._standard_item_name(item_to_be_removed)
        if item_to_be_removed not in self.cart:
            print("Item not found in cart.")
            return
        current_quantity = self.cart[item_to_be_removed]
        if current_quantity > 1 and confirm_action("Do you want to reduce quantity instead of full removal?"):
            item_quantity_to_reduce = self._get_valid_quantity(
                f"Enter quantity to reduce from {item_to_be_removed.capitalize()} (max {current_quantity}): ",
                current_quantity
            )
            if item_quantity_to_reduce:
                if confirm_action(f"Confirm removing {item_quantity_to_reduce} from {item_to_be_removed.capitalize()}?"):
                    self.cart[item_to_be_removed] -= item_quantity_to_reduce
                    self.inventory.increase_item_quantity(item_to_be_removed, item_quantity_to_reduce)
                    if self.cart[item_to_be_removed] == 0:
                        self.cart.pop(item_to_be_removed)
                    print(f"Removed {item_quantity_to_reduce} {item_to_be_removed.capitalize()}.")
                return
            else:
                print("Operation cancelled or too many failed attempts.")
                return
        if confirm_action(f"Remove all {current_quantity} {item_to_be_removed.capitalize()}?"):
            self.inventory.increase_item_quantity(item_to_be_removed, current_quantity)
            self.cart.pop(item_to_be_removed)
            print(f"Removed all {item_to_be_removed.capitalize()} from cart.")
        else:
            print("Retry later.")