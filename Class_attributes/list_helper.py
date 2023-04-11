# WRITE YOUR SOLUTION HERE:

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):

        x = 0
        counted = 0
        for num in my_list:
            if my_list.count(num) > counted:
                counted = my_list.count(num)
                x = num

        return x

    @classmethod
    def doubles(cls, my_list: list):

        doubles = []
        u = []
        for num in my_list:
            if num not in doubles:
                doubles.append(num)
            else:
                u.append(num)

        doubles2 = []
        for num in u:
            if num not in doubles2:
                doubles2.append(num)

        return len(doubles2)

if __name__ == "__main__":

    numbers = [1, 1, 1, 2, 2, 3]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))