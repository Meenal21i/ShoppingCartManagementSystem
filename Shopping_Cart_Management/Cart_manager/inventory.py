from static.validator import is_valid_item_name
from interfaces.addables import ItemAdder
from interfaces.printable import ItemPrinter

class Inventory(ItemAdder, ItemPrinter):
    def __init__(self):
        self.items = {}

    def _standard_item_name(self, item_name):
        return item_name.strip().lower()
    
    def _is_valid_item(self, item_name, item_quantity=None):
        if not is_valid_item_name(item_name):
            raise ValueError("Please enter a valid item name.")
        if item_quantity is None or item_quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
    def add_item(self, item_name, item_quantity):
        item = self._standard_item_name(item_name)
        self._is_valid_item(item, item_quantity)
        if item in self.items:
            self.items[item] += item_quantity
        else:
            self.items[item] = item_quantity

    def if_item_exists(self, item_to_be_checked):
        return self._standard_item_name(item_to_be_checked) in self.items
    
    def current_quantity(self, item_name):
        item = self._standard_item_name(item_name)
        return self.items.get(item, 0)
    
    def reduce_item_quantity(self, item_to_be_reduced, item_quantity):
        item = self._standard_item_name(item_to_be_reduced)
        if self.items[item] >= item_quantity:
            self.items[item] -= item_quantity

    def increase_item_quantity(self, item_to_be_increased, item_quantity):
        item = self._standard_item_name(item_to_be_increased)
        self.items[item] = self.items[item] + item_quantity

    def print_items(self):
        if not self.items:
            print("Inventory is empty!")
        else:
            print("\nAvailable Inventory:")
            for item_name, item_quantity in self.items.items():
                print(f"{item_name.capitalize()}: {item_quantity}")