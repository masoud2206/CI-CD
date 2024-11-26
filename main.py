def sayhi(name):
    print(f"HI {name}")

def admin(username):
    if username == "admin":
        print("Welcome Admin")

def username(password):
    if password == 1234:
        print("Logged In Successfully")


def test_sayhi():
    assert sayhi("ali") == "HI ali"



def test_admin():
    assert admin("admin") == "Welcome Admin"



def test_username():
    assert username(1234) == "Logged In Successfully"