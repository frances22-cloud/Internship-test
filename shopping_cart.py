
cart = []  

def add_item(name, price, quantity=1):
    cart.append((name, price, quantity))
    print(f"Added: {quantity} × {name} (${price:.2f} each)")

def remove_item(name):
    global cart
    cart = [item for item in cart if item[0].lower() != name.lower()]
    print(f"Removed all {name} from cart")

def calculate_total():
    subtotal = sum(price * qty for _, price, qty in cart)
    return subtotal

def total_price():
    subtotal = calculate_total()
    
    if subtotal > 100:
        discount = subtotal * 0.10
        final = subtotal - discount
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"10% discount applied: -${discount:.2f}")
        print(f"Total Price: ${final:.2f}")
    else:
        print(f"Total: ${subtotal:.2f} (no discount)")
    
    return final if subtotal > 100 else subtotal

def show_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nCart contents:")
    for name, price, qty in cart:
        print(f"- {name}: {qty} × ${price:.2f} = ${price * qty:.2f}")
    total_price()