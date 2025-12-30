from store.models import PhysicalProduct, DigitalProduct
from store.operations import Order

def add_products_interactively(order):
    print("Welcome to the Smart Inventory Store!")
    print("Add items to your cart. Type 'done' when finished.\n")

    while True:
        action = input("Do you want to add a product? (yes/done): ").strip().lower()
        if action in ['done', 'no', 'exit', 'quit']:
            break
        if action != 'yes':
            print("Please type 'yes' or 'done'")
            continue

        name = input("Enter product name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue

        try:
            price = float(input("Enter price(₦): "))
            if price < 0:
                print("Price cannot be negative!")
                continue
        except ValueError:
            print("Please enter a valid number for price.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be at least 1!")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        product_type = input("Is this a physical or digital product? (p/d): ").strip().lower()

        if product_type in ['p', 'physical']:
            try:
                weight = float(input("Enter weight in kg: "))
                if weight <= 0:
                    print("Weight must be positive!")
                    continue
                product = PhysicalProduct(name, price, weight)
            except ValueError:
                print("Invalid weight. Skipping this item.")
                continue

        elif product_type in ['d', 'digital']:
            download_link = input("Enter download link (e.g., https://example.com/ebook.pdf): ").strip()
            if not download_link:
                download_link = "https://example.com/download"  
            product = DigitalProduct(name, price, download_link)

        else:
            print("Invalid type! Please enter 'p' or 'd'. Skipping this item.")
            continue

        order.add_item(product, quantity)
        print(f"✅ Added: {quantity}x {name}\n")

    print("Cart finalized!\n")

def enhanced_checkout(order):
    if not order.cart:
        print("Your cart is empty!")
        return

    total = 0
    physical_items = []
    digital_items = []

    for entry in order.cart:
        prod = entry['item']
        qty = entry['qty']
        cost = prod.get_total_price(qty)
        total += cost

        item_line = f"{prod._name} (x{qty}): ₦{cost}"
        if isinstance(prod, PhysicalProduct):
            shipping_cost = prod.weight * 200 * qty
            item_line = f"{prod._name} (x{qty}, {prod.weight}kg each): ₦{cost:.2f} (includes ₦{shipping_cost:.2f} shipping)"
            physical_items.append(item_line)
        else:  
            item_line = f"{prod._name} (x{qty}): ₦{cost:.2f}"
            link_line = f"   📎 Download: {prod.download_link}"
            digital_items.append(item_line)
            digital_items.append(link_line)
    
    print("=" * 40)
    print("           RECEIPT")
    print("=" * 40)

    if physical_items:
        print("📦 PHYSICAL PRODUCTS:")
        for line in physical_items:
            print("   " + line)
        print()

    if digital_items:
        print("💾 DIGITAL PRODUCTS:")
        for line in digital_items:
            print("   " + line)
        print()

    print("-" * 40)
    print(f"{'GRAND TOTAL':<30} ₦{total}")
    print("=" * 40)

def run_store():
    my_order = Order()
    add_products_interactively(my_order)
    enhanced_checkout(my_order)

if __name__ == "__main__":
    run_store()