import sys
import utils
import passchecker
import storage

database = storage.load_database()

while True:
    print("===========================")
    print("       ENTER YOUR CHOICE    ")
    print("  1. ADD PASSWORD    ")
    print("  2. DELETE PASSWORD")
    print("  3. VIEW PASSWORD  ")
    print("  4. PASSWORD STRENGTH CHECKER ")
    print("  0. EXIT           ")
    print("===========================")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        utils.addpassword(database)
        storage.save_database(database)
    elif choice == 2:
        utils.deletepassword(database)
        storage.save_database(database)
    elif choice == 3:
        utils.viewpassword(database)
    elif choice == 4:
        passchecker.passcheckstrength()
    elif choice == 0:
        print("\nExiting program. Goodbye!")
        sys.exit() 
    else:
        print("\n[Error] Invalid Choice, please try again.\n")

