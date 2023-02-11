# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):

    # Length validation
    if len(pic) != 11:
        return False

    # Century marker validation
    year = 0

    if pic[6] == "A":
        year = 2000
    
    elif pic[6] == "-" :
        year = 1900

    elif pic[6] == "+":
        year = 1800

    else:
        return False

    year += int(pic[4:6])
    print(year)

    # Date validation
    try:
        date = datetime(year, int(pic[2:4]), int(pic[0:2]))
        print(date)
    except:
        return False

    # Control character validation
    control_characters_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    nine_digits = int(pic[0:6]+pic[7:10])
    index_string = str(nine_digits/31).split(".")
    index = round(float(f"0.{index_string[1]}") * 31)

    char = control_characters_string[index]
    print(char)

    if char == pic[-1]:
        return True
    else:
        return False

if __name__ == "__main__":

    print(is_it_valid("030103A493DD"))