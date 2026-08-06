def addpassword(db):
    website = input("Enter Website Name: ").strip()
    user = input("Enter Username : ").strip()
    password = input("Enter Password : ").strip()

    if not website or not user or not password :
        print("All fields must not be empty:")

    db[website] = {
        "username" : user,
        "password" : password
    }

def viewpassword(db):
    print(db)

def deletepassword(db):
    item = input("Enter Website Name: ")
    confirm = input("Enter 'Confirm' To Delete: ")
    if confirm == "Confirm":
        del db[item]
        print("Password Deleted Successfully!")
    else:
        print("Confirmation Failed!")