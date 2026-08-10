import sys
import utils
import passchecker
import passgenerator
import storage
import bcrypt
import os
import keygen

database = storage.load_database()
MASTER_KEY_FILE = "master.key"

if not os.path.exists(MASTER_KEY_FILE):
    print("===================================")
    print("      FIRST TIME INITIALIZATION    ")
    print("===================================")
    print("Set a Master Password. 'This password is very Important!'\n")
    
    new_master = input("Create Master Password: ").strip()
    
    if not new_master:
        print("\n[Error] Master password cannot be empty. Exiting.")
        sys.exit()

    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(new_master.encode('utf-8'), salt)
    
    with open(MASTER_KEY_FILE, "wb") as f:
        f.write(hashed)

    del new_master
       
    print("\nMaster Password saved successfully!\n")


else:
    with open(MASTER_KEY_FILE, "rb") as f:
        stored_hash = f.read()

    print("===================================")
    print("        AUTHENTICATION REQUIRED    ")
    print("===================================")
    attempt = input("Enter Master Password to Unlock: ").strip()
    
    if not bcrypt.checkpw(attempt.encode('utf-8'), stored_hash):
        print("\n[Error] Incorrect Master Password. Access Denied!")
        sys.exit()

    key = keygen.encryption_key_gen(attempt)

    del attempt
       
    print("\nAccess Granted!\n")


while True:
    print("===================================")
    print("       ENTER YOUR CHOICE    ")
    print("  1. ADD PASSWORD    ")
    print("  2. DELETE PASSWORD")
    print("  3. VIEW PASSWORD  ")
    print("  4. PASSWORD STRENGTH CHECKER ")
    print("  5. PASSWORD GENERATOR        ")
    print("  0. EXIT           ")
    print("===================================")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        utils.addpassword(database,key)
        storage.save_database(database)
    elif choice == 2:
        utils.deletepassword(database)
        storage.save_database(database)
    elif choice == 3:
        utils.viewpassword(database,key)
    elif choice == 4:
        passchecker.passcheckstrength()
    elif choice ==5:
        passgenerator.generate_pass()
    elif choice == 0:
        print("\nExiting program. Goodbye!")
        sys.exit() 
    else:
        print("\n[Error] Invalid Choice, please try again.\n")

