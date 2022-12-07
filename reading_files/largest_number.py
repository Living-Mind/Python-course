# write your solution here
def largest():

    with open("numbers.txt") as new_file:
    
        new_list = [] 
    
        for line in new_file:
            line = int(line.replace("\n", ""))
            #print(line)
            new_list.append(line)
            new_list.sort()
        print(new_list[-1])
        return new_list[-1]




if __name__ == "__main__":

    largest()
    