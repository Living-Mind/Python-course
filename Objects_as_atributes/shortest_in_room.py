# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
        #print(person.height)

    def is_empty(self):
        if len(self.persons) == 0:
            return True 
        else:
            return False

    def print_contents(self):
        sum_h = 0
        for person in self.persons:
            sum_h += person.height
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {sum_h} cm')

        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')

    def shortest(self):

        shortest_person = "None"
        current_height = 0
        if shortest_person == "None" and len(self.persons) > 0:

            for person in self.persons:

                if shortest_person == "None":
                    shortest_person = person
                    current_height = person.height

                else:
                    if person.height < current_height:
                        current_height = person.height
                        shortest_person = person
        else:
            return None

        return shortest_person

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest = self.shortest()
            self.persons.remove(shortest)
            return shortest

if __name__ == "__main__":

    #Part1
   # room = Room()
   # print("Is the room empty?", room.is_empty())
   # room.add(Person("Lea", 183))
   # room.add(Person("Kenya", 172))
   # room.add(Person("Ally", 166))
   # room.add(Person("Nina", 162))
   # room.add(Person("Dorothy", 155))
   # print("Is the room empty?", room.is_empty())
   # room.print_contents()

    #Part2
   # room = Room()
   # print("Is the room empty?", room.is_empty())
   # print("Shortest:", room.shortest())
   # 
   # room.add(Person("Lea", 183))
   # room.add(Person("Kenya", 172))
   # room.add(Person("Nina", 162))
   # room.add(Person("Ally", 166))
   # 
   # print()
   # 
   # print("Is the room empty?", room.is_empty())
   # print("Shortest:", room.shortest())
   # 
   # print()
   # 
   # room.print_contents()

    #Part3
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()
    
    print()
    
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
    
    print()
    
    room.print_contents()