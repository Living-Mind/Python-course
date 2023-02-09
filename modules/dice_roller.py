# Write your solution here
import random

def roll(die: str):

    die_A = (3, 3, 3, 3, 3, 6)
    die_B = (2, 2, 2, 5, 5, 5)
    die_C = (1, 4, 4, 4, 4, 4)

    if die == "A":

        return random.choice(die_A)

    elif die == "B":
        
        return random.choice(die_B)

    elif die == "C":

        return random.choice(die_C)

def play(die1: str, die2: str, times: int):

    die1_wins = 0
    die2_wins = 0
    ties = 0

    for n in range(times):

        value1 = roll(die1)
        value2 = roll(die2)

        if value1 > value2:
            die1_wins += 1
        elif value1 < value2:
            die2_wins += 1
        elif value1 == value2:
            ties += 1

    return (die1_wins, die2_wins, ties)

if __name__ == "__main__":
    #print(roll("A"))
    print(play("A", "C", 30))
