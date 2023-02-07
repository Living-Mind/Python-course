# Write your solution here
import string

def separate_characters(my_string: str):

    ascii_char = ""
    punctuation_char = ""
    other_char_list = []
    other_char = ""

    for c in my_string:


        if c in string.ascii_letters:

            ascii_char += c

        elif c in string.punctuation:

            punctuation_char += c

        else:
            other_char_list.append(c)

        
    for i in other_char_list:
        other_char += i

    return (ascii_char, punctuation_char, other_char)

if __name__ == "__main":

    parts = separate_characters("Varmista, että koodin suoritus onnistuu")
    print(parts[0])