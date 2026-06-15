menu={"pretzel": 4.50,
      "pizza": 50,
      "burger": 75,
      "soda": 5,
      "subway": 100,
      "icecream": 20}

cart=[]
total=0

print("-------- MENU --------")
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
print()
while True:
    food=input("Enter the item you would like to buy (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- Your Order --------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: {total:.2f}")