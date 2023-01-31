# Write your solution here
def find_words(search_term: str):

    with open("words.txt") as new_file:

        found_words = []

        for line in new_file:

            if search_term[0] == "*":

                if line.strip().endswith(search_term[1:]):

                    found_words.append(line.strip())

            elif search_term[-1] == "*":

                if line.strip().startswith(search_term[0:-1]):

                    found_words.append(line.strip())

            elif search_term == line.strip():

                found_words.append(search_term)

    return found_words

if __name__ == "__main__":
    #print(find_words("*at"))
    print(find_words("ca*"))
    print(find_words("cat"))

            
