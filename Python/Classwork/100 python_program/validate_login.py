# Predefined username and password
correct_username = "admin"
correct_password = "1234"

# Read input
username = input("Enter username: ")
password = input("Enter password: ")

# Validate username and password
if username == correct_username and password == correct_password:
    print("Login Successful - validate_login.py:11")
else:
    print("Invalid Username or Password - validate_login.py:13")


    '''output:'''
    Enter username: admin
    Enter password: 1234
    Login Successful