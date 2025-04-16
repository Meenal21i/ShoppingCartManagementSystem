from config import PAYMENT_METHODS, PAYMENT_METHOD_CREDIT, PAYMENT_METHOD_DEBIT
from static.handlers import confirm_action, read_input
from auth.authentication import Authenticator
import random

class CheckoutProcessor:
    def __init__(self, shopping_cart, user_password):
        self.cart = shopping_cart
        self.stored_password = user_password
        
    def checkout_process(self):
        if not self.cart.cart:
            print("Cart is empty. Please enter items in cart before checkout.")
            return
        password_input = read_input("Enter password to confirm checkout: ", allow_cancel=False)
        if password_input != self.stored_password:
            print("Incorrect password. Checkout aborted.")
            return
        print("\nSelect payment method:")
        for key, value in PAYMENT_METHODS.items():
            print(f"{key}. {value}")
        payment_method_key = read_input("Enter payment method number: ")
        if payment_method_key not in PAYMENT_METHODS:
            print("Invalid payment method. Aborting.")
            return
        payment_method = PAYMENT_METHODS[payment_method_key]
        if not confirm_action(f"You selected '{payment_method}'. Confirm?"):
            print("Checkout cancelled.")
            return
        if payment_method in [PAYMENT_METHOD_CREDIT, PAYMENT_METHOD_DEBIT]:
            card_number = read_input(f"Enter your {payment_method} Number: ",allow_cancel=False)
            print(f"{payment_method} ending with {card_number[-4:]} has been charged.")
            print("Payment successful! Order placed.")
        else:
            address = read_input("Enter delivery address: ", allow_cancel=False)
            print(f"Order will be delivered to: {address}")
        print("Estimated delivery will be within ", random.randint(3, 9), " days!")
        self.cart.clear_cart()