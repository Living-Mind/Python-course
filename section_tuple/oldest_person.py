# Write your solution here
def oldest_person(people: list):

    oldest = 0
    name = ""

    for person in people:
        if oldest == 0:
            oldest = person[1]
            name = person[0]

        elif oldest > person[1]:
            oldest = person[1]
            name = person[0]

    return name

if __name__ == "__main__":

    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    
    print(oldest_person(people))
