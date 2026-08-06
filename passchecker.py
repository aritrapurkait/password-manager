def passcheckstrength():
    password = input("Enter Your Password: ").strip()
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0
    for char in password:
         if "a" <= char <= "z":
              lowercase_count += 1
         elif "A" <= char <= "Z":
              uppercase_count += 1
         elif "0" <= char <= "9":
              digit_count += 1
         else:
              special_count += 1
    total_length = len(password)

    if total_length >= 8 and lowercase_count > 0 and uppercase_count > 0 and digit_count > 0 and special_count > 0:
         print("Strong Password (Great mix of characters!)")
    elif total_length >= 6 and (lowercase_count > 0 or uppercase_count > 0) and digit_count > 0:
         print("Medium Password")
    else:
         print("Weak Password (Too short or missing character variety)")
