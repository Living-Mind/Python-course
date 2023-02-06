# Write your solution here
def filter_incorrect():

    with open("lottery_numbers.csv") as new_file:

        for line in new_file:

            string_split = line.strip().split(" ")
            values_split = string_split[1].split(";")
            
            lottery_nums = values_split[1].split(",")

            try:

                num_list = []
                dict_lottery = {}

                week_num = int(values_split[0])

                for n in lottery_nums:

                    number = int(n)

                    if number > 0 and number < 39:

                        num_list.append(number)

                    else:

                        continue

                if len(num_list) != 7: 

                    raise ValueError()

                if len(num_list) != len(set(num_list)):  

                    raise ValueError()

                else:
                    dict_lottery[week_num] = num_list

                with open("correct_numbers.csv", 'a') as new_file:

                    new_file.write(f'week {week_num};{str(dict_lottery[week_num]).replace(" ", "").strip("[]")}\n')

            except ValueError:
                pass



if __name__ == "__main__":
    filter_incorrect()