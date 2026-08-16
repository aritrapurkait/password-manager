import string
import secrets 

def generate_pass():
    try:
        length = int(input("Enter Password Length (Min 8) : "))
    except ValueError:
        print("Length Must Be Integer! ")
        return

    if length < 8:
        print("Too Short Length! ")
        return

    special_char = '!@#$%&*'

    guranteed_pool = [secrets.choice(string.ascii_uppercase),secrets.choice(string.ascii_lowercase),secrets.choice(string.digits),secrets.choice(special_char)]

    pool = string.ascii_letters + string.digits + special_char

    remaining_length = (length - len(guranteed_pool))
    remaining = []
    for i in range(remaining_length):
        remaining.append(secrets.choice(pool))

    pass_list = guranteed_pool + remaining


    for i in range(len(pass_list)-1,0,-1):
        j = secrets.randbelow(i+1)
        pass_list[i],pass_list[j] = pass_list[j],pass_list[i]

    generated_pass = "".join(pass_list[:length])

    print("Generated Password is: ",end="")
    print(generated_pass)
    return