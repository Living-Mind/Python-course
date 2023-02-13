# Write your solution here
import json

def print_persons(filename: str):

    with open(filename) as new_file:

        data = new_file.read()

        people = json.loads(data)

        for person in people:

            formated_hobbies = str(person["hobbies"]).strip("[]").replace("'", "")

            print(f'{person["name"]} {person["age"]} years ({formated_hobbies})')

if __name__ == "__main__":
    print(print_persons("file1.json"))