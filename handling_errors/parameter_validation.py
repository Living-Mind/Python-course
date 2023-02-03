# Write your solution here
def new_person(name: str, age: int):

    if age < 0 or age > 150:
        raise ValueError("Age Problem")


    
    if name == "" or " " not in name or len(name) > 40:
        raise ValueError("Name Problem")

    values = (name, age)
    return values


if __name__ == "__main__":

    values = new_person("Bob Alice", 30)
    print(values)
