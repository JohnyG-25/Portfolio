# In the review, I was told to not use global variables. However it is the only way I can get active_user to carry across all functions. Why should I avoid them?

import time     
import calendar
from datetime import date
import datetime

def login():                                             
    """Login display function"""   
    list_users()               
    
    login_bool = True                                       
    while(login_bool):                                              
        username = input("Please input your username: ")            
        if check_username(username):            
            
            check_pass = check_user_password(username)              
            password = input("Please input your password: ")        
            if password == check_pass:                              
                global active_user                                  
                active_user = username
                report_gen()                                        
                menu(active_user)                                   
                login_bool = False                                  
            else :
                print("Password is incorrect. Please try again")    
        else:
            print("User does not exist")                           

def check_username(username): 
    """Return True if username in user.txt"""   
    with open("user.txt", "r+") as f:                         
        for line in f:                                          
            temp_user = (line.split(", "))[0]                   
            if username == temp_user:                           
                f.close()                                      
                return True                                    

def check_user_password(username):                                  
    """Return password for given username"""   
    with open("user.txt", "r+") as f:                           
        for line in f:
            if username in line:                                               
                password = (line.split(", "))[1]
                password = password.replace("\n", "")               
                f.close()
                return password                                     

def list_users():                                                   
    """Generate list of users from user.txt""" 
    global users_lists                                              
    users_lists = []
    with open("user.txt", "r+") as f:                               
        for line in f:
            temp_user = (line.split(", "))[0]     
            users_lists.append(temp_user)    

def menu(active_user):                                              
    '''Menu display function'''   
    print("Welcome " + active_user)                                 
    menu_bool = True                                                
    while menu_bool:                                               
        if active_user == "admin":                                  
            menu = input('''\n\nSelect one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            u - Userlist
            s - Stats
            g - Generate a report
            e - Exit
            l - Logout
            : ''').lower()
            if menu == "r": 
                reg_user()
            elif menu == "u":
                print(users_lists)
            elif menu == "a":
                add_task()
            elif menu == "s":
                stats()
            elif menu == "g":                 
                report_gen()                                        
            elif menu == "va":     
                view_all_tasks()
            elif menu == "vm":       
                view_my_tasks(active_user, True)
            elif menu == "e": 
                print("Goodbye " + active_user)
                exit()                                              
                break
            elif menu == "l": 
                login()
            else :
                print("That is not a valid choice. Please try again")

        if active_user != "admin":                                  
            menu = input('''\n\nSelect one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit
            l - logout
            : ''').lower()
            if menu == "a":
                add_task()
            elif menu == "va":     
                view_all_tasks()
            elif menu == "vm":       
                view_my_tasks(active_user, True)
            elif menu == "e": 
                print("Goodbye " + active_user)
                break
                exit()
            elif menu == "l": 
                login()
            else :
                print("That is not a valid choice. Please try again")

def reg_user():                                                                        
    """Add a new user to user.txt"""   
    reg_bool = True
    while reg_bool:
        print("\n\nRegistering a user.")
        username = input("Please input a username: ")                                       
        if (check_username(username)) :                                                     
            print("This user already exists")        
        else:
            password_1 = input("Please input a password for that user: ")                   
            password_2 = input("Please confirm your password for that user: ")
            if password_1 == password_2:                                                    
                new_user_string = "\n" + str(username) + ", " + str(password_1)             
                print("Enrolling " + username + " With the password: " + password_1)        
                with open("user.txt", "a") as f:                                            
                    f.write(new_user_string)                                                
                    time.sleep(0.6)                                                         
                    print("User enrolled.")                                                 
                    users_lists.append(username)                                            
                    f.close()                                                               
                    break                                                        
            else:
                print("Passwords dont match. Please try again")                             

def add_task():                                                                                                             
    """Add a new task to task.txt"""                                                                                        
    username = input("Who are you assigning the task to?: ")                                                                
    if username in users_lists:                                                                                             
        label = input("Please give a task label: ")                                                                         
        description = input("Please give a task description: ")
        date_now = input("Please input the current date in the following format.\nDD Mon YYYY\t:")
        if check_date_format(date_now):
            due_date = input("Please input the due date the following format.\nDD Mon YYYY\t:")
            if check_date_format(due_date):                                                                                 
                completed = input("Has the task been completed? Yes or No: ")
                new_task_string = "{}, {}, {}, {}, {}, {}".format (
                username,
                label, 
                description, 
                date_now, 
                due_date, 
                completed)     

                print("New task has been created\n\n")                                                                                  
                format_task(new_task_string.split(", "))                                                                            
                with open("tasks.txt", "a") as f:                                                                                   
                    f.write("\n" + new_task_string)
            else:   
                print("Sorry, that format is incorrect. Please try again")
        else:   
            print("Sorry, that format is incorrect. Please try again")
    else:   
        print("That user does not exist")

def view_my_tasks(user, edit):                                  
    """Dispalys all tasks belonging to user"""
    with open("tasks.txt", "r+") as f:                          
        task_num = 1 
        my_tasks = []
        for line in f:                                          
            task = line.split(", ")                             
            if (task[0] == user):                               
                my_tasks.append(line)                           
                print("\n\n")                                   
                print("Task number:\t\t" + str(task_num))
                format_task(task)                               
                task_num = task_num + 1                         
        if (edit):
            task_menu(my_tasks)                                 

def view_all_tasks():                                       
    task_num = 1                                            
    with open("tasks.txt", "r+") as f:                      
        for line in f:                                      
            task = line.split(", ")     
            print("\n\n")                   
            print("Task number:\t\t" + str(task_num))       
                          
            
            format_task(task)                               
            task_num = task_num + 1

def task_menu(tasks):                                                                                   
    '''Creates an input menu for tasks. This is where you can edit tasks, and mark them as completed'''
    menu = input('''\n\nSelect one of the following Options below:
    ed - \tEdit a task
    c  - \tMark a task as completed
    e - \tExit the program
    menu -\tGo back to the menu
    : ''').lower()

    if menu == "ed":
        choice = input("Which task would you like to edit? Please only input the task number: ")
        edit_task(tasks[int(choice) - 1])                                                                   
    elif menu == "c":
        choice = input("Which task would you like to mark as complete? Please only input the task number: ")
        mark_complete(tasks[int(choice) - 1])                                                             
    elif menu == "e": 
        print("Goodbye " + active_user)
        menu_bool = False
        exit()
    elif menu == "menu": 
        pass
    else :
        print("That is not a valid choice. Please try again")

def edit_task(task):                                            
    '''Allows user to edit a task'''
    task_list = task.split(", ")                                

    if ("No" in task_list[5]):                                  
        choice = input('''\nWhat would you like to change?      
user - The user the task is assigned to.
date - The date the task is due for.
''').lower()                                                    
        if choice == "user":                                    
            new_user = input('''
Who would you like to assign this task to? Your choices are'''
+ str(users_lists) + "\n")                              
            if (check_username(new_user)):

                new_user_string = "{}, {}, {}, {}, {}, {}".format (
                    new_user, 
                    task_list[1], 
                    task_list[2], 
                    task_list[3], 
                    task_list[4], 
                    task_list[5])  

                replace_in_file(task, new_user_string)                                                                                              
        if choice == "date":                                                                                                                        
            new_date = input("What would you like to change the due date to? ")

            new_date_string = "{}, {}, {}, {}, {}, {}".format (
                task_list[0], 
                task_list[1], 
                task_list[2], 
                task_list[3], 
                new_date, 
                task_list[5])    

            replace_in_file(task, new_date_string)
    elif ("Yes" in task_list[5]):                               
        print("You cannot edit a task that has been completed")
    else:  
        print("Something went wrong")

def mark_complete(task):                                    
    '''marks a task as complete'''
    task_list = task.split(", ")                                                                                                        
    new_task_string = "{}, {}, {}, {}, {}, Yes\n".format (
        task_list[0], 
        task_list[1], 
        task_list[2], 
        task_list[3], 
        task_list[4])         

    replace_in_file(task, new_task_string)                                                                                              

def replace_in_file(old_string, new_string):                
    '''Replaces a string in tasks.txt with another string'''
    f = open("tasks.txt", "r")                              
    data = ""                                               
    for line in f:                                          
        new_data = line.replace(old_string, new_string)     
        data = data + new_data                              
    f.close()                                               
    f = open("tasks.txt", "w")                              
    f.write(data)                                           
    f.close()                                               

def stats():                                                    
    '''Print stats from reports file'''
    print("\n\n\n")
    with open("user_overview.txt", "r") as f:                               
        for line in f:                                                          
            print(line, end = "")
        f.close()
    with open("task_overview.txt", "r") as f:                               
        for line in f:
            print(line, end = "")
        f.close()

def format_task(task):                              
    """Displays a task in a neat way"""
    print("Username:\t\t" + task[0])
    print("Task Label:\t\t" + task[1])
    print("Date assigned:\t\t" + task[3])
    print("Date task is due:\t" + task[4])
    print("Task Discription:\t" + task[2])
    print("Task completed?\t\t" + task[5])

def retrieve_task_data(user):
    '''Function that retrieves data from tasks.txt, and builds a report'''
    with open("tasks.txt", "r+") as f:              

        my_tasks = ""           
        report_string = ""
        total_tasks = 0
        total_user_tasks = 0
        user_percentage = 0
        complete_percentage = 0
        incomplete_percentage = 0
        overdue_tasks = 0
        overdue_percentage = 0
        com = 0
        incom = 0

        for line in f:                                  
            total_tasks = total_tasks + 1  
            task = line.split(", ")

            if (task[0] == user):                       
                my_tasks = my_tasks + line              
                total_user_tasks = total_user_tasks + 1 
                incom = my_tasks.count("No")            
                com = my_tasks.count("Yes")             
                print(task[4])
                if check_if_overdue(task[4]):
                    overdue_tasks = overdue_tasks + 1
                    print("overdue")
        
        if total_user_tasks > 0:                                            
            user_percentage = (total_user_tasks / total_tasks) * 100
            complete_percentage = (com / total_user_tasks) * 100
            incomplete_percentage = (incom / total_user_tasks) * 100
            overdue_percentage = (overdue_tasks / total_user_tasks) * 100
   
        report_string = '''
Tasks assigned =\t{}
Tasks completed =\t{}
Tasks incomplete =\t{}
Tasks overdue =\t{}
Percentage of total tasks owned by user :\t{}%
Percentage of user tasks coompleted by user :\t{}%
Percentage of user tasks incomplete by user :\t{}%
Percentage of user tasks overdue by user :\t{}%
'''.format(
total_user_tasks,com,incom,overdue_tasks,
round(user_percentage, 2),
round(complete_percentage, 2),
round(incomplete_percentage, 2),
round(overdue_percentage, 2))

        return(report_string)   

def report_gen():                           
    '''Function to generate a report'''
    tasks = open("tasks.txt", "r+")         
    total_tasks = 0                         
    complete_tasks = 0                      
    incomplete_tasks = 0                    
    overdue_total = 0
    incom_overdue_total = 0
    incomplete_percent = 0
    for line in tasks:                      
        task = line.split(", ")             
        total_tasks = total_tasks + 1       
        if "No" in task[5] :                        
            incomplete_tasks = incomplete_tasks + 1
        if "Yes" in task[5] :                       
            complete_tasks = complete_tasks + 1
        if check_if_overdue(task[4]):
            overdue_total = overdue_total + 1
        if check_if_overdue(task[4]) and "No" in task[5]:
            incom_overdue_total = incom_overdue_total + 1    

    overdue_percent = (overdue_total / total_tasks) * 100
    incomplete_percent = (incomplete_tasks / total_tasks) * 100

    task_report_string = '''
Total tasks =\t\t\t{}
Completed tasks =\t\t{}
Incomplete tasks =\t\t{}
Overdue tasks = \t\t{}
Overdue incomplete tasks = \t{}
Overdue tasks percentage = \t{}
Incomplete tasks percentage = \t{}

'''.format(total_tasks,
complete_tasks,
incomplete_tasks,
overdue_total,
incom_overdue_total,
overdue_percent,
incomplete_percent
)  
    with open("task_overview.txt", "w") as t_file:                              
        t_file.write(task_report_string)                                        

    with open("user_overview.txt", "w") as u_file:                              
        u_file.write("Total users =\t" + str(len(users_lists)))                 
        u_file.write("\nTotal Tasks =\t" + str(total_tasks) + "\n")             
        for i in range(len(users_lists)):                                       
            u_file.write("\nTasks for " + users_lists[i] + ":\n")               
            u_file.write(retrieve_task_data(users_lists[i]))                    

def check_date_format(date):
    '''Checks if the inputted date is a valid format. If it is, return true'''
    try:
        temp_date = (date.lower()).split()
        abr_month = temp_date[1][0].upper() + temp_date[1][1:3]
        temp_date[1] = (list(calendar.month_abbr).index(abr_month))
        temp_date[0] = int(temp_date[0])
        temp_date[2] = int(temp_date[2])
        print(temp_date)
    except ValueError:
        print("Date format is incorrect")
        return (False)

    return(True)

def convert_date(date):
    '''Converts date to a usable format. Basically a copy of check_date_format'''
    try:
        temp_date = (date.lower()).split()
        abr_month = temp_date[1][0].upper() + temp_date[1][1:3]
        temp_date[1] = (list(calendar.month_abbr).index(abr_month))
        temp_date[0] = int(temp_date[0])
        temp_date[2] = int(temp_date[2])
        return(temp_date)
    except ValueError:
        print("Date format is incorrect")

def check_if_overdue(due_date):
    '''Compares a "duedate" to systems current date, and checks if duedate is before system date
    If so, returns true (is overdue)'''
    
    due_date = convert_date(due_date)
    today = date.today()
    current_date = today.strftime("%d, %m, %Y")
    current_date = current_date.split(", ")
    for i in range(len(current_date)):
        current_date[i] = int(current_date[i])

    current_temp = datetime.datetime(current_date[2], current_date[1], current_date[0])
    due_temp = datetime.datetime(due_date[2], due_date[1], due_date[0])
      
    if current_temp < due_temp:
        return(False)
    elif current_temp >= due_temp:
        return(True)

login()                                             

