# Write your solution here
def create_tuple(x: int, y: int, z: int):

    new_list = [x, y, z]
    new_list.sort()
    a = new_list[0]
    b = new_list[-1]
    c = sum(new_list)
    
    new_tuple = (a, b, c)

    return new_tuple




if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
