unit=input("Enter unit of temperature either Celsius(C) or Fahrenheit(F):" )
if unit=="C":
    temp=float(input("Enter temperature in Celsius:"))
    F=((9/5)*temp)+32
    print(f"Temperature in Fahrenheit is {F}")
elif unit=="F":
    temp=float(input("Enter temperature in Fahrenheit"))
    C=(temp-32)/1.8
    print(f"Temperature in Fahrenheit is {C}")
else:
    print("Invalid unit of temperature")