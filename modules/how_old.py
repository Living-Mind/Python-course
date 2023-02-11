# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

bdate = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)

diff = millennium_eve - bdate

if diff.days > 0:
    print(f"You were {diff.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
