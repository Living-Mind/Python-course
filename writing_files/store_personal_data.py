# Write your solution here
def store_personal_data(person: tuple):
    #print(f'{person[0]};{person[1]};{person[2]}')

    with open("people.csv", "a") as new_file:
        new_file.write(f'{person[0]};{person[1]};{person[2]}')



if __name__ == "__main__":
    store_personal_data(("Bob Lazar", 36, 172.2))


