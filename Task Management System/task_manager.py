# Authers Notes
# I have used functions for this entire task. I dont like using nested if statements, and without functions, thats all this would end up being. Giant messy ifififif statements. 
# I have skipped documentation for all the basic code. This includes self explanatory code. Example (login_bool = True)
# I am very curious to know how this would look without functions

# Imports       
import time     # Import time library to use sleep function

# Login
def login():                                                        # Create function for user to login with
    """Login display function"""   
    list_users()                                                    # Uses List_users function to create a list of users in user.txt
    login_bool = True                                               
    while(login_bool):                                              
        username = input("Please input your username: ")            # Gets user input for username
        if check_username(username):                                # Uses check_username function to check if username is in user.txt
            check_pass = check_user_password(username)              # Retrieves the password from user.txt for that use
            password = input("Please input your password: ")        # Gets user input for password
            if password == check_pass:                              # If user input is the same as Retrieved password
                global active_user                                  # Creates a global variable called active_user and sets that to the username input. We will use this active_user later
                active_user = username
                menu(active_user)                                   # Calls the menu function with the active user variable
                login_bool = False                                  # Ends the login loop
            else :
                print("Password is incorrect. Please try again")    # If password was entered incorrectly
        else:
            print("User does not exist")                            #If username was entered incorrectly

def check_username(username):                                   # Create function to check if given perameter is inside of user.txt as a user. Not as a password. Returns a bool
    """Return True if username in user.txt"""   
    with open("user.txt", "r+") as f:                           # Open file
        for line in f:                                          # Repeats for every line in file
            temp_user = (line.split(", "))[0]                   # Seperates each line into a username and password, and sets the username to temp_user
            if username == temp_user:                           # Basic iff statement
                f.close()                                       # Closes the file. We are done with it
                return True                                     # Ends the function, and returns true 

def check_user_password(username):                                  # Retreives the password for given username. Function is almost identical to function above. Returns a string
    """Return password for given username"""   
    with open("user.txt", "r+") as f:                           
        for line in f:
            if username in line:                                               
                password = (line.split(", "))[1]
                password = password.replace("\n", "")               # Removes the \n(next line) from the end of the password
                f.close()
                return password                                     # Return the password

def list_users():                                                   # Create a function to generate a list of users from user.txt, aswell as any users registered while the code is running.
    """Generate list of users from user.txt""" 
    global users_lists                                              # Global variable "users_lists" creation
    users_lists = []
    with open("user.txt", "r+") as f:                               # Opens user.txt. Seperates the username and password for every line. Adds every username to users_lists. Closes the file afterwards
        for line in f:
            temp_user = (line.split(", "))[0]     
            users_lists.append(temp_user)    

def menu(active_user):                                              # Create a function to generate a menu. Uses a if statement to generate a different menu for admin user
    """Menu display function"""   
    print("Welcome " + active_user)                                 # Basic print
    menu_bool = True                                                # Control variable
    while(menu_bool):                                               # While true
        if active_user == "admin":                                  # This if statement runs for admins. Choices for them include registering a user, and viewing the full userlist, above the standard choices. 
            menu = input('''\n\nSelect one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            u - Userlist
            s - Stats
            e - Exit
            l - Logout
            : ''').lower()
            if menu == "r": 
                register_user()
            elif menu == "u":
                print(users_lists)
            elif menu == "a":
                add_task()
            elif menu == "s":
                 stats()
            elif menu == "va":     
                view_all_tasks("a")
            elif menu == "vm":       
                view_all_tasks("m")
            elif menu == "e": 
                print("Goodbye " + active_user)
                menu_bool = False                                   # Closes the menu loop. 
                exit()                                              # Exit function. Closes the terminal
            elif menu == "l": 
                login()
            else :
                print("That is not a valid choice. Please try again")

        if active_user != "admin":                                  # This if statement runs for everyone that is NOT admin. Functionally the same as above
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
                view_all_tasks("a")
            elif menu == "vm":       
                view_all_tasks("m")
            elif menu == "e": 
                print("Goodbye " + active_user)
                menu_bool = False
                exit()
            elif menu == "l": 
                login()
            else :
                print("That is not a valid choice. Please try again")

def register_user():                                                                        # Function to register a new user.
    """Add a new user to user.txt"""   
    reg_bool = True
    while reg_bool:
        print("\n\nRegistering a user.")
        username = input("Please input a username: ")                                       # Username input
        if (check_username(username)) :                                                     # Cannot register a user that already exists
            print("This user already exists")        
        else:
            password_1 = input("Please input a password for that user: ")                   # 2x inputs for passwords. Incase user cant spell
            password_2 = input("Please confirm your password for that user: ")
            if password_1 == password_2:                                                    # Compares both password inputs
                new_user_string = "\n" + str(username) + ", " + str(password_1)             # Creates a string for both passwords. 
                print("Enrolling " + username + " With the password: " + password_1)        # Basic print
                with open("user.txt", "a") as f:                                            # Opens user.txt
                    f.write(new_user_string)                                                # Writes the new user to text file, at the ned of existing code
                    time.sleep(0.6)                                                         # The code waits for 0.6 seconds. For dramatic effect
                    print("User enrolled.")                                                 
                    users_lists.append(username)                                            # Adds this new user to users_lists. 
                    f.close()                                                               # Closes the file
                    reg_bool = False                                                        # CLoses the registration loop
            else:
                print("Passwords dont match. Please try again")                             # User cant spell

def add_task():                   
    """Add a new task to task.txt"""                                                                                        # Function to add a new task
    username = input("Who are you assigning the task to?: ")                                                                # Basic input for username
    if username in users_lists:                                                                                             # Checks user input, if inside users_lists. Cannot assign tasks to users that dont exist
        label = input("Please give a task label: ")                                                                         # Gets input for task details, for label, description, dates, and if completed
        description = input("Please give a task description: ")
        date_now = input("Please input the current date: ")
        due_date = input("Please input the due date: ")
        completed = input("Has the task been completed? Yes or No: ")
        new_task_string = "{}, {}, {}, {}, {}, {}".format (username, label, description, date_now, due_date, completed)     # Creates a new string, using format function
        print("New task has been created")                                                                                  # Prints stuff
        format_task(new_task_string.split(", "))                                                                            # Uses the format_task function, to display the new task
        with open("tasks.txt", "a") as f:                                                                                   # Writes the new task to tasks.txt
            f.write("\n" + new_task_string)
    else: 
        print("That user does not exist")

def view_all_tasks(type):                   # Function to view all tasks. Uses an if statement, and parameters when function is called, to define what tasks are to be viewed 
    """Dispalys all tasks requested.Type can either be "a" (all) or "m" (mine)"""
    with open("tasks.txt", "r+") as f:      # Opens file                     
        for line in f:                      # Loop for every line
            if type == "a":                 # If type == a ( We want to see all tasks )
                task = line.split(", ")     
                format_task(task)           # Uses format_task function to display each task
            if type == "m":                 # If type == m ( We want to see my tasks )
                task = line.split(", ")
                if (task[0] == active_user):# Only selects tasks belonging to active user
                    format_task(task)       # Uses format_task function to display each task

def stats():                                                    # Function that displays total users, along with a list of users. Also displays total tasks
    """Gets a list of stats for all users and tasks"""
    print("\n\nTotal Users =\t" + str(len(users_lists)))        # Prints total number of users in users_lists
    print("\nUsers: \n", end = "")                              # Basic print
    for i in range(len(users_lists)):                           # For loop. Repeats for every user in users_lists
        print("\t" + users_lists[i])                            # Basic print
    print("")                                                   # Basically a \n

    with open("tasks.txt", "r+") as t:                          # Opens tasks.txt
        total_tasks = 0                                         # Variable set to 0
        for line in t:                                          # Loop for every line in tasks
            total_tasks = total_tasks + 1                       # total_tasks increase by 1
    print("Total Tasks =\t" + str(total_tasks))                 # Print total tasks

def format_task(task):                              # Function to dispaly a task. Uses print functions, and tabs to keep it neat
    """Displays a task in a neat way"""
    print("\nUsername:\t\t" + task[0])
    print("Task Label:\t\t" + task[1])
    print("Date assigned:\t\t" + task[3])
    print("Date task is due:\t" + task[4])
    print("Task Discription:\t" + task[2])
    print("Task completed?\t\t" + task[5])

#Actual Code that runs
login()                                             # Calls the login function. This is the second line of code that actually runs

# So close to 200 lines.