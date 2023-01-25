# Write your solution here
#1
#2


def search_by_name(filename: str, word: str):

    name_list = []
    list_match = []

    with open(filename) as new_file:

        for line in new_file:

            if line[0].isupper(): 
                name_list.append(line.strip())

    for i in name_list:

        if i.lower().find(word) >= 0:
            list_match.append(i)

    print(list_match)     
    return list_match


def search_by_time(filename: str, prep_time: int):

    name = ""
    dict_recipe = {}
    name_list = []
    values = []
    exercise_list = []
    i = 0

    with open(filename) as new_file:

        for line in new_file:

            if line[0].isupper():
                name_list.append(line.strip())
                
            elif line[0].isdigit():
                values.append(line.strip())

        for name in name_list:
            dict_recipe[name] = int(values[i])
            i += 1

        for recipe in dict_recipe:
            if dict_recipe[recipe] <= prep_time:
                #print(f'{recipe}, preparation time {dict_recipe[recipe]}')
                exercise_list.append(f'{recipe}, preparation time {dict_recipe[recipe]} min')
                
        print(exercise_list)
        return exercise_list

if __name__ == "__main__":

    #search_by_name("recipes1.txt", "cake")
    search_by_time("recipes1.txt", 20)