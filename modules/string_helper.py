# Write your solution here
def change_case(orig_string: str):

    new_string = ""
    
    for letter in orig_string:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()

    return new_string

def split_in_half(orig_string: str):

    length = len(orig_string)
    #print(length)
    mid = int(length/2)
    #print(mid)

    return orig_string[:mid], orig_string[mid:]
            
def remove_special_characters(orig_string: str):

    new_string = ""

    for letter in orig_string:
        if letter.isalpha() or letter.isalnum() or letter == " ":
            new_string += letter

    return new_string


if __name__ == "__main__":
    print(split_in_half("abcdefg"))
    print(remove_special_characters("Test! Ok!"))