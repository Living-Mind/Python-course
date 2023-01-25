# Write your solution here
#1


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

    time_dict = {}
    time_list = []
    name = ""
    time = 0

    with open(filename) as new_file:

        for line in new_file:
            if line.strip().isdigit(): 
                time = int(line.strip())
                print("time here")
                #print(line.strip())
                print(name)
                print(time)
                time_dict[name] = time
                time_list.append(name)

            name = line.strip()


            #if prep_time <= time:
            #    print(f'{name}, preparation time {time} min')
            print(time_dict)
            print(time_list)
            print(time_dict.get("Pancakes"))
        for n in time_list:
            if prep_time <= time_dict.get(n):
                print("ok")



if __name__ == "__main__":

    #search_by_name("recipes1.txt", "cake")
    search_by_time("recipes1.txt", 30)