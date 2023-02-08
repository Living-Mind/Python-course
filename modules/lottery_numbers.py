# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):

    number_range_list = list(range(lower, upper+1))
    weekly_draw = sample(number_range_list, amount)
    return sorted(weekly_draw)


if __name__ == "__main__":

    print(lottery_numbers(3, 1, 20))