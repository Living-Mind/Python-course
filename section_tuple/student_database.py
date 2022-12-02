# Write your solution here
def add_student(students: dict, student: str):

    students[student] = []



def print_student(students: dict, student: str):

    if student in students:
        if students[student] == []:
            print(f'{student}: \n no completed courses')
        else:
            grade = 0
            completed_courses = len(students[student])

            print(f'{student}:')
            print(f' {completed_courses} completed courses:')
            for s_course in students[student]:
                print(f'  {s_course[0]} {s_course[1]}')
                grade += s_course[1]
            print(f' average grade {grade / completed_courses}')
                
            
            #print(students[student])
    else:
        print(f'{student}: no such person in the database')

def add_course(students: dict, student: str, course: tuple):

    students[student].append(course)
    
    #students[student] = [course]


if __name__ == "__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")