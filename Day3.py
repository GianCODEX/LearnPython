name = input("Enter your gadget name: ")
price = float(input("Enter device price: "))

available_input = input("Is the gadget available? (yes/no): ").strip().lower()
on_sale_input = input("Is the gadget on sale? (yes/no): ").strip().lower()
defective_input = input("Is the gadget defective? (yes/no): ").strip().lower()

available = available_input == 'yes'
on_sale = on_sale_input == 'yes'
defective = defective_input == 'yes'

print(f"\nGadget: {name}\nPrice: ₱{price:.2f}", type(price))

if available:
    print("Available: True")
else:
    print("Available: False")

if available and on_sale:
    print("Gadget is ON SALE")
elif on_sale and defective:
    print("Gadget is NOT DEFECTIVE")
elif available and on_sale and defective:
    print("Gagdet is NOT AVAILABLE")
else:
    print("Gadget is DEFECTIVE")
    
choices = input("\nWill you purchase this device? (yes/no): ").strip().lower()
if choices == 'yes':
    choice = input("Enter confirmation: (yes/no): ").strip().lower()
    if choice == 'yes':
        print(f"\nYOU HAVE PURCHASED: {name}\n")

        your_Cart = "YOUR CART"
        print("=" * 50)
        print(your_Cart.center(50))
        print("-" * 50)

        print(f"{name.title():<20}{'Qty':>5}{'Unit Price':>25}")
        print(f"{'':<20}{quantity:>5}{price:>25.2f}")
        
        total = price * quantity
        
        print("-" * 50)
        print(f"{'Grand Total:':<40}{total:>10.2f}")
        print("=" * 50)
    else:
        print("You have canceled the transaction...")
else:
    print("No purchase made.")
