foods=[]
prices=[]
total=0

while True:
    food=input("Enter food you would like to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of {food}:"))
        foods.append(food)
        prices.append(price)

print("------YOUR CART-----")
# for food in foods:
#     print(food, end=" ")

# print()

# for price in prices:
#     print(price, end=" ")
#     total += price
# print()

# for food,price in zip(foods,prices):
#     print(f"{food}: {price}")

# for price in prices:
#     total += price
    
cart=[food, price]
print(cart)
print(f"your total is {total}")
