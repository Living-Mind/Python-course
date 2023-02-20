# Write your solution here
def average(person: dict):

    result_sum = (person["result1"] + person["result2"] + person["result3"])
    return result_sum/3

def smallest_average(person1: dict, person2: dict, person3: dict):

    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2
        
    if average(person3) < average(smallest):
        smallest = person3

    return smallest

if __name__ == "__main__":

    person1 = {"name": "Bob", "result1": 1, "result2": 5, "result3": 3}
    person2 = {"name": "Alice", "result1": 4, "result2": 7, "result3": 1}
    person3 = {"name": "Corg", "result1": 7, "result2": 2, "result3": 8}

    print(smallest_average(person1, person2, person3))
