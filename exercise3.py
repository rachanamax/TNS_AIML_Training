# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]

# Customer shopping cart
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]


# 1. Build the Inventory
def build_inventory(raw_delivery):
    inventory = {}

    for product, price, quantity in raw_delivery:
        if product in inventory:
            inventory[product]["stock"] += quantity
        else:
            inventory[product] = {
                "price": price,
                "stock": quantity
            }

    return inventory


# Create inventory
inventory = build_inventory(raw_delivery)

print("Inventory:")
print(inventory)


# 2. Process the Shopping Cart
receipt = []

for product in shopping_cart:

    if product not in inventory:
        print(product, "is not carried in this store")

    elif inventory[product]["stock"] == 0:
        print(product, "is sold out!")

    else:
        inventory[product]["stock"] -= 1

        price = inventory[product]["price"]
        receipt.append((product, price))


# 3. Generate the Receipt
print("\nReceipt:")
print(receipt)

total_price = 0

for product, price in receipt:
    total_price += price

print("Total price:", total_price)
