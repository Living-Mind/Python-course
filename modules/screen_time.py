# Write your solution here
from datetime import datetime, timedelta 

file_name = str(input("Filename: "))

with open(file_name, "a") as new_file:

    start_date = str(input("Starting date: "))
    
    days = int(input("How many days: "))
    
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    
    formated_start_date = datetime.strptime(start_date, "%d.%m.%Y")
    one_day = timedelta(days=1)
    formated_date = formated_start_date.strftime("%d.%m.%Y")
    
    days_list = []
    
    total_minutes = 0
    
    for day in range(days):
    
        screen_time = str(input(f'Screen time {formated_date}: ').replace(" ", "/"))
    
        days_list.append(f'{formated_date}: {screen_time}')
        formated_start_date += one_day
        formated_date = formated_start_date.strftime("%d.%m.%Y")
        
        # Minutes calculation
        screen_time_split = screen_time.split("/")
        total_minutes += int(screen_time_split[0]) + int(screen_time_split[1]) + int(screen_time_split[2])
    
    average_minutes = total_minutes/days
    
    time_period = f'Time period: {(days_list[0])[0:10]}-{(days_list[-1])[0:10]}'
    
    # Appending to file 
    new_file.write(f'{time_period}\n')
    new_file.write(f'Total minutes: {total_minutes}\n')
    new_file.write(f'Average minutes: {average_minutes}\n')

    for n in days_list:
        new_file.write(f'{n}\n')

    new_file.close()

    print(f"Data stored in file {file_name}")
