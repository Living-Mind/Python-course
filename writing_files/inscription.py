# Write your solution here
name = input("Whom should I sign this to: ")
file_name = input("Where shall I save it: ")

print(name)
print(file_name)

with open(file_name, "w") as my_file:
    my_file.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

