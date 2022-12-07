def matrix_sum():

    #print(sum(row_sums()))
    return sum(row_sums())


def matrix_max():

    element_list = []

    #print(rows())
    for row in rows():
        for element in row:
            element_list.append(element)

    element_list_sorted = sorted(element_list)
    #print(element_list_sorted[-1])

    return element_list_sorted[-1]

            




def rows():

    new_list = []

    with open("matrix.txt") as new_file:

        for line in new_file:

            deeper_list = []
            line = line.replace("\n", "")
            values = line.split(",")

            for value in values:
                deeper_list.append(int(value))

            new_list.append(deeper_list)

    #print(new_list[0])
    return new_list

def row_sums():

    #print(rows()[0])

    row_sums_list = []

    for row in rows():
        #print(row)
        row_sums_list.append(sum(row))
    #print(row_sums_list)

    return row_sums_list


if __name__ == "__main__":

    #rows()
    #row_sums()
    print(matrix_sum())
    #print(matrix_max())

