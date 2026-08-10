import keygen
import base64


def addpassword(db,key):
    website = input("Enter Website Name: ").strip()
    user = input("Enter Username : ").strip()
    raw_password = input("Enter Password : ").strip()

    if not website or not user or not raw_password :
        print("All fields required ")
        return

    cipher = keygen.AES.new(key, keygen.AES.MODE_CBC)
    ciphered_pass = cipher.encrypt(keygen.pad(raw_password.encode('utf-8'), keygen.AES.block_size))

    encrypted_b64_pass = base64.b64encode(ciphered_pass).decode('utf-8')
    iv_b64 = base64.b64encode(cipher.iv).decode('utf-8')

    db[website] = {
        "username" : user,
        "password" : encrypted_b64_pass,
        "iv" : iv_b64
    }
    print(f"\nPassword encrypted and saved for '{website}' successfully. \n")


def viewpassword(db,key):
    webname = input("Enter Website Name: ").strip()
    
    if webname not in db:
        print(f"\n[Error] No password found for '{webname}'.\n")
        return

    try:

        encrypted_pass_bytes = base64.b64decode(db[webname]['password'])
        iv_bytes = base64.b64decode(db[webname]['iv'])


        cipher = keygen.AES.new(key, keygen.AES.MODE_CBC, iv=iv_bytes)


        decrypted_padded = cipher.decrypt(encrypted_pass_bytes)
        plain_password = keygen.unpad(decrypted_padded, keygen.AES.block_size).decode('utf-8')


        print(f"\nWebsite : {webname}")
        print(f"Username: {db[webname]['username']}")
        print(f"Password: {plain_password}\n")

    except (KeyError, ValueError) as e:
        print(f"\n[Error] Failed to decrypt password. (Incorrect key or corrupted data)\n")

def deletepassword(db):
    item = input("Enter Website Name: ")
    confirm = input("Enter 'Confirm' To Delete: ")
    if confirm == "Confirm":
        del db[item]
        print("Password Deleted Successfully!")
    else:
        print("Confirmation Failed!")