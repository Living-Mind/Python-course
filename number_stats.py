# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum_calc = 0

    def add_number(self, number:int):
        #pass
        self.numbers += 1
        self.sum_calc += number

    def count_numbers(self):
        #pass
        counted_numbers = self.numbers
        return counted_numbers
        #return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        else:
            return self.sum_calc

        
    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return self.sum_calc/self.count_numbers()


#stats = NumberStats()
#stats.add_number(3)
#stats.add_number(5)
#stats.add_number(1)
#stats.add_number(2)
#print("Numbers added:", stats.count_numbers())
#print("Sum of numbers:", stats.get_sum())
#print("Mean of numbers:", stats.average())

stats = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()

while True:
    
    user_input = int(input("Please type in integer numbers: "))
    
    if user_input != -1:
    
        stats.add_number(user_input)

        if user_input %2 == 0:
            stats_even.add_number(user_input)
        else:
            stats_odd.add_number(user_input)
        
    else:
        break

#print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())