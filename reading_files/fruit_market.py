# write your solution herne.splite
def read_fruits():

    with open("fruits.csv") as new_file:

        new_dictionary = {}

        for line in new_file:
            line = line.replace("\n", "")
            fields = line.split(";")
            #print(fields)
            new_dictionary[fields[0]] = float(fields[1])

        return new_dictionary




        





if __name__ == "__main__":

    read_fruits()
