username=input("Enter a username:")
if len(username)>12:
    print("Your username cant contain more than 12 characters")
elif username.find(" "):
    print("your username cant contain spaces")
elif not username.isalpha():
    print("your username can't contain digits")
else:
    print(f"{username}")