# Write your solution here:
class Clock:
    def __init__(self, h: int, m: int, s: int):
        self.h = h
        self.m = m
        self.s = s


    def set(self, set_h: int, set_m: int):
        self.h = set_h
        self.m = set_m
        self.s = 0

    def tick(self):

        if self.h == 23 and self.m == 59 and self.s == 59:
            self.h = 0
            self.m = 0
            self.s = 0

        elif self.m == 59 and self.s == 59:
            self.m = 0
            self.s = 0
            
        elif self.s == 59:
            self.m += 1
            self.s = 0

        else:
            self.s += 1

    def __str__(self):
        return f'{self.h:02}:{self.m:02}:{self.s:02}'
    
if __name__ == "__main__":

    clock = Clock(23, 59, 55)
    
    print(clock)
    clock.tick() 
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    #clock.set(12, 2)
    print(clock)
    clock.tick()
    print(clock)
