MAX_QUANTITY_RETRIES = 3
DEFAULT_CART_LIMIT = 3
MENU_OPTIONS = {
    1: "View Inventory",
    2: "Add to Cart",
    3: "Remove from Cart",
    4: "View Cart",
    5: "Checkout",
    6: "Exit"
}
EXIT_CHOICE = len(MENU_OPTIONS)
VALID_MENU_CHOICES = range(1, EXIT_CHOICE + 1)
PAYMENT_METHOD_CREDIT = "Credit Card"
PAYMENT_METHOD_DEBIT = "Debit Card"
PAYMENT_METHOD_CASH = "Cash on Delivery"
PAYMENT_METHODS = {
    "1": PAYMENT_METHOD_CREDIT,
    "2": PAYMENT_METHOD_DEBIT,
    "3": PAYMENT_METHOD_CASH
}