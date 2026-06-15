# # print("I like pizza")
# #string
# first_name="Vedanshi"
# food="burger"
# print(f"hello {first_name}")
# print(f"you like {food}")

# #integers
# age=25
# print(f"you are {age} years old")

# #float
# price=10.99

# #Boolean
# is_student=True
# print(f"Are you a student?: {is_student}")

# name="Vedanshi Parmar"
# age=19
# gpa=9.7
# is_student=True


# gpa=int(gpa)
# print(gpa)

# age=str(age)

# age +="1"
# print(age)

# name=input("what is your name?:")
# print(f"hello {name}!")

# a=5
# b=6
# print(a+b)

# #in the below code th answer is 56 bcz when we use input then it returns value in string
# a=input("Enter first number: ")
# b=input("Enter second number: ")
# print(f"addition is: {a+b}")

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"addition is: {a+b}")

# print(f"the area is {area} cm²")

#Exercise 2 Shopping cart
# item=input("what item would you like to buy?: ")
# price=float(input("What is the price?: "))
# quantity=int(input("How many would you like to buy?: "))
# total=price*quantity

# print(f"You have brought {quantity} x {item} so your total is {total}")

# x=3
# y=5
# z=4.8
# result=round(x)
# result=abs(y) #abs means absolute mtlb negative integer positive ho jata hai
# result=pow(4,3)
# result=max(x,y,z)
# result=min(x,y,z)
# print(result)


# import math
# x=9.9
# print(math.pi)
# print(math.e)
# result=math.sqrt(x)
# result=math.ceil(x) #round to upper digit which means 9.1 rounds to 10
# result=math.floor(x) #round to lower digit which means 9.1 rounds to 9 

# import math
# a=float(input("Enter side A:"))
# b=float(input("Enter side B:"))
# c=math.sqrt(pow(a,2)+pow(b,2))
# print(f"side c:{round(c,2)}")


# age=int(input("enter your age:"))
# if age>=18:
#     print("you are applicable for license")
# else:
#     print("you are not applicable")


# response = input("would you like some food? (Y/N):")
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")
name=input("Enter your name")
result = name.find(" ")
# result = name.rfind(" ")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result=name.isdigit()
# result = name.isalpha()
print(result)