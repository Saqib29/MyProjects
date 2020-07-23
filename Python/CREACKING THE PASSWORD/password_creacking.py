from module_of import check_password

password = input("Enter password: ")
guess_password = check_password(password)
if guess_password == password:
    print("password found ", password)
else:
    print(guess_password)
