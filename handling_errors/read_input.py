# Write your solution here
def read_input(input_str: str, num1: int, num2: int):
    while True:
        try:
            input_str = input("Please type in a number: ")
            number = int(input_str)
            if number > num1 and number < num2:
                return number
        except ValueError:
            pass


        print(f"You must type in an integer between {num1} and {num2}")


if __name__ == "__main__":

    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
