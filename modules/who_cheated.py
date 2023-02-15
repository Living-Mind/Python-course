# Write your solution here
import datetime
import csv

def cheaters():

    students_start_time = {}
    students_submission = {}
    students_name_list = []
    cheaters_list = []

    with open("start_times.csv") as start_time_file:
        for line in csv.reader(start_time_file, delimiter=';'):
            students_start_time[line[0]] = line[1]
            students_name_list.append(line[0])

    with open("submissions.csv") as submissions_file:

        for line in csv.reader(submissions_file, delimiter=";"):
            if line[0] in students_submission.keys():
                if line[3] > students_submission[line[0]]:
                    students_submission[line[0]] = line[3]
            else:
                students_submission[line[0]] = line[3]
            #x = students_submission[line[0]]
            #print(x)

    for student in students_name_list:

        time_calc = (datetime.datetime.strptime(students_start_time[student], "%H:%M")) + datetime.timedelta(hours=3)
        formated_submission = (datetime.datetime.strptime(students_submission[student], "%H:%M"))

        #print(student)
        #print(f'Start {students_start_time[student]}')
        #print(time_calc)
        #print(formated_submission)

        if time_calc < formated_submission:
            cheaters_list.append(student)
            #print(f'cheat {student}')
            

    return list(set(cheaters_list))

if __name__ == "__main__":

    print(cheaters())