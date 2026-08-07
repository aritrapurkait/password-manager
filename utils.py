def addpassword(db):
    website = input("Enter Website Name: ").strip()
    user = input("Enter Username : ").strip()
    password = input("Enter Password : ").strip()

    if not website or not user or not password :
        print("All fields required ")
        return

    db[website] = {
        "username" : user,
        "password" : password
    }

def viewpassword(db):
    webname = input("Enter Website Name: ")
    if webname in db:
        print(f"\nWebsite: {webname}")
        print(f"Username: {db[webname]['username']}")
        print(f"Password: {db[webname]['password']}\n")
    else:
        print(f"\n[Error] No password found for '{webname}'.\n")

def deletepassword(db):
    item = input("Enter Website Name: ")
    confirm = input("Enter 'Confirm' To Delete: ")
    if confirm == "Confirm":
        del db[item]
        print("Password Deleted Successfully!")
    else:
        print("Confirmation Failed!")