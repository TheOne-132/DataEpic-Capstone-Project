class Order:
    def __init__(self):
        self.cart = []

    def add_item(self, product, quantity):
        self.cart.append({'item': product, 'qty': quantity})

    def checkout(self):
        total = 0
        print("--- Receipt ---")
        for entry in self.cart:
            prod = entry['item']
            qty = entry['qty']
            cost = prod.get_total_price(qty)
            total += cost
            print(f"{prod._name} (x{qty}): ₦{cost}")
        print(f"Grand Total: ₦{total}")