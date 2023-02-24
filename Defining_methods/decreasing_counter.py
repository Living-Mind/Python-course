# Tee ratkaisusi tähän:
class DecreasingCounter:

    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        #pass
        
        if self.value == 0:
            pass
        else:
            self.value -= 1

    def set_to_zero(self):

        self.value = 0

    def reset_original_value(self):
        
        #print(self.original)

        self.value = self.original

    # Write the rest of the methods here!

if __name__ == "__main__":

    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()