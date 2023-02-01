# Write your solution here

while True:

    print("1 - Add word, 2 - Search, 3 - Quit")

    function = int(input("Function: "))

    if function == 1:

        word_fin = str(input("The word in Finnish: "))
        word_en = str(input("The word in English: "))

        with open("dictionary.txt", "a") as new_file:
            
            new_file.write(f'{word_fin};{word_en}\n')

        print("Dictionary entry added")

    elif function == 2:

        search_term = str(input("Search term: "))

        with open("dictionary.txt") as read_file:

            for line in read_file:

                if search_term in line.strip():

                    word = line.strip().split(";")

                    print(f'{word[0]} - {word[1]}')


    elif function == 3:

        print("Bye!")
        break
