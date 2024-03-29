# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

#class Box:
#    def __init__(self):
#        self.sum_weight = 0
#        self.presents = []
#
#    def add_present(self, present: Present):
#        self.present = present
#        self.presents.append(present)
#
#    def total_weight(self):
#
#        self.sum_weight += self.present.weight
#        return self.sum_weight

class Box:

    def __init__(self):

        self.presents = []

 

    def add_present(self, present: Present):

        self.presents.append(present)

 

    def total_weight(self):

        weight = 0

        for present in self.presents:

            weight += present.weight

        return weight

if __name__ == "__main__":

   # book = Present("ABC Book", 2)
   # 
   # print("The name of the present:", book.name)
   # print("The weight of the present:", book.weight)
   # print("Present:", book)

    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())
    
    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())