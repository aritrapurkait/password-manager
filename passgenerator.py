import random
import string

def generate_pass():
    length = int(input("Enter Password Length: "))

    pool = (string.ascii_uppercase,string.ascii_lowercase,string.digits,string.punctuation)

    generated_pass = ""

    for i in range(length):
        setchoice = random.choice(pool)
        generated_pass += random.choice(setchoice)

    print("Generated Password is: ",end="")
    print(generated_pass)
    return