def sayhi(name):
    print(f"HI {name}")

def admin(username):
    if username == "admin":
        print("Welcome Admin")

def username(user):
    name = input("Enter your Username: ")
    if user == name:
        print("Logged In Successfully")