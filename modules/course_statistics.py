# Write your solution here
import urllib.request
import json

def retrieve_all():

    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    
    json_format = json.loads(data)
    
    active_courses_list = []
    
    for course in json_format:
    
        if course["enabled"] == True:
            #print(course)
    
            course_tuple = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            #print(course_tuple)
    
            active_courses_list.append(course_tuple)
    
    return active_courses_list

def retrieve_course(course_name: str):

    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    
    data = my_request.read()
        
    json_format = json.loads(data)
    
    weeks = 0
    students = 0
    hours_total = 0
    exercises = 0
    
    for week in json_format:
    
        students += ((json_format[week])["students"])
        hours_total += ((json_format[week])["hour_total"])
        exercises += ((json_format[week])["exercise_total"])
        weeks += 1
        
    exercises_average = round(exercises/students)
    hours_average = round(hours_total/students)
    
    course_dict = {}
    
    course_dict["weeks"] = weeks
    course_dict["students"] = students
    course_dict["hours"] = hours_total 
    course_dict["hours_average"] = hours_average 
    course_dict["exercises"] = exercises 
    course_dict["exercises_average"] = exercises_average 
    
    print(course_dict)
    return course_dict

if __name__ == "__main__":

    #print(retrieve_all())
    retrieve_course("docker2019")
