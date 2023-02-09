# Write your solution here
import random

def words(n: int, beginning: str):

    with open("words.txt") as new_file:

        words_list = []
        chosen_words = []

        for line in new_file:

            if line.strip().startswith(beginning):
                words_list.append(line.strip())

        try:

            for i in range(n):
            
                chosen_words.append(random.choice(words_list)) 

        except:

            raise ValueError()

    return chosen_words

if __name__ == "__main__":

    print(words(10, "des"))