weight=float(input("Enter your weight: "))
unit=input("Kilograms(Kg) or pounds(L): ")
if unit=="Kg":
    L=weight*2.20462
    print(f"Your weight in pounds is {round(L,2)}")
elif unit=="L":
    Kg=weight/2.20462
    print(f"Your weight in kgs is {round(Kg,2)}")
else:
    print("Unit is invalid")
