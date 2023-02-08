# Write your solution here
from random import choice
import string

def generate_password(length: int):

    password = ""

    char_list = list(string.ascii_lowercase[:])

    for i in range(length):

        password += choice(char_list)
    
    return password
    
if __name__ == "__main__":
    print(generate_password(20))



