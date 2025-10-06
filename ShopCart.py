
foods = []
prices = []
your_Cart = "YOUR CART"
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: ₱"))
        foods.append(food)
        prices.append(price)
        
print("=" * 50)
print(your_Cart.upper().center(50))
print("-" * 50)

for i in range(len(foods)):
    print(f"{foods[i]:<30} ₱{prices[i]:>10.2f}")

print("-" * 50)
total = sum(prices)
print(f"{'Total:':<30} ₱{total:>10.2f}")
print("=" * 50)
