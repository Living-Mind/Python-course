# Write your solution here
def filter_solutions():

    open("correct.csv", 'w').close()
    open("incorrect.csv", 'w').close()

    with open("solutions.csv") as new_file:
        
        for line in new_file:

            part = line.strip().split(";")
            name = part[0]
            problem = part[1]
            result = part[2]

            if "-" in problem:

                digits = problem.split('-')
                solution = int(digits[0])-int(digits[1])

                if int(solution) == int(result):

                    with open("correct.csv", "a") as my_file:
                        my_file.write(f'{line.strip()}\n')

                else:
                    
                    with open("incorrect.csv", "a") as my_file:
                        my_file.write(f'{line.strip()}\n')


            elif "+" in problem:

                digits = problem.split('+')
                solution = int(digits[0])+int(digits[1])

                if int(solution) == int(result):

                    with open("correct.csv", "a") as my_file:
                        my_file.write(f'{line.strip()}\n')

                else:
                    
                    with open("incorrect.csv", "a") as my_file:
                        my_file.write(f'{line.strip()}\n')

if __name__ == "__main__":
    filter_solutions()