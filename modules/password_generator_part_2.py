# Write your solution here
from random import choice
import string

def generate_password(length: int, digits: bool, special_char: bool):

    password = ""

    char_list = list(string.ascii_lowercase[:])

    if digits == True:

        digit_list = list(string.digits)
        
        char_list.extend(digit_list)

        
    if special_char == True:
        
        special_char = ["!","?","=","+","-","(",")","#"]
        
        char_list.extend(special_char)

    for i in range(length):

        password += choice(char_list)

    return password
    
if __name__ == "__main__":
    print(generate_password(2, False, False))
