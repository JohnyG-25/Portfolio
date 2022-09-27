#Import time library for sleep function
import time

#Shoes List
shoe_list = []

# Defines the "Shoes" object
class Shoes(object):
    '''Creates class object Shoe'''
    def __init__(self,country, code, product, cost,quantity): 
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        self.value = int(quantity) * int(cost)

    def get_cost(shoe):
        '''Returns the cost of the shoe'''
        # While i understand the purpose of this method, I prefer to just use .cost
        return(shoe.cost)
        
    def get_quanty(shoe): #Spelt like this as requested in task. I think it was a typo
        # While i understand the purpose of this method, I prefer to just use .quantity
        '''Returns the quantity of the shoe'''
        return(shoe.quantity)

    def __str__(self):
        '''Defines the string representation of the object. This is what will be displayed when using print function'''
        string = f'''Location:\t{self.country}
Code:\t\t{self.code}
Product:\t{self.product}
Cost:\t\tR{self.cost}
Quantity:\t{self.quantity}
'''

        return(string)

def read_shoes_data():
    '''Adds all shoes inside inventory.txt to shoe_list as objects'''
    try:
        f = open("inventory.txt", "r")   
    except:
        raise Exception("File doesnt exist")                           
    for line in f:
        if "Country,Code,Product,Cost,Quantity" in line:
            pass
        else:
            try:
                line_list = line.split(",")
                line_list[4].replace("\n", "")
            except:
                print("The line\n" + line + "\nIs in the wrong format. Skipping this line")
            try:
                shoe = Shoes(line_list[0], line_list[1], line_list[2], line_list[3],line_list[4].replace("\n", ""))
                shoe_list.append(shoe)
            except:
                print("Could not complete the task. Skipping this line")
    f.close()

def capture_shoes():
    '''country, code, product, cost,quantity)'''
    country = input("What is the location?:\t\t")
    code = input("What is the shoe code?:\t\t")
    product = input("What is the shoe called?:\t")
    cost = input("What is the shoe cost?:\t\t")
    quantity = input("How many shoes are in stock?:\t")
    shoe = Shoes(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():
    '''Prints every shoe. 
This is displayed in a formatted way because we defined the string representation in the object class blueprint'''
    for i in range(len(shoe_list)):
        print(shoe_list[i])

def re_stock():
    '''Function to re-stock the lowest stocked shoe. Uses min_max() function'''
    lowest = min_max()[0]
    for i in range(len(shoe_list)):
        if str(shoe_list[i].quantity).replace("\n", "") == lowest:
            print("The lowest stock item is the following: ")
            print(shoe_list[i])
            choice = input("Would you like the update that quantity? (yes or no):\t").lower()
            if choice == "yes": 
                new_stock = int(input("What is the new stock of that shoe?"))
                shoe_list[i].quantity = new_stock

def min_max():
    '''Gets the highest and lowest stock counts, and returns them in a list'''
    stock_list = []
    for i in range(len(shoe_list)):
        count = str(shoe_list[i].quantity)
        count = count.replace("\n", "")
        stock_list.append(int(count))
    lowest = sorted(stock_list)[0]
    highest = sorted(stock_list)[-1]
    min_max_list = [str(lowest),str(highest)]
    return(min_max_list)

def search_shoe(code):
    '''Searches shoe list for a coded shoe. Prints that item information'''
    for i in range(len(shoe_list)):
        if shoe_list[i].code == code:
            print(shoe_list[i])

def value_per_item():
    '''Gets all values of all items and prints them in a string'''
    # Im not completely sure what was requested of me here, however I completed it as I understood it
    for i in range(len(shoe_list)):
        cost = shoe_list[i].cost
        quantity = int(shoe_list[i].quantity)
        name = shoe_list[i].product
        value = shoe_list[i].value
        string = "For the {}, there is a total of {}. Each one costs {}, to a total value of {}".format(name,quantity,cost,value)
        print(string)

def highest_qty():
    '''Gets the highest stocked shoe, and puts a 10% sale on it'''
    highest = min_max()[1]
    for i in range(len(shoe_list)):
        if shoe_list[i].quantity.replace("\n", "") == highest:
            print("The shoe with the highest quantity is the following")
            print(shoe_list[i])
            new_price = int(shoe_list[i].cost) - (int(shoe_list[i].cost) / 10)
            shoe_list[i].cost = str(new_price)
            print("Shoe is now on sale for 10% off.")
            print(shoe_list[i])

def menu():
    '''Displays a menu. Uses a while loop to keep menu active'''
    read_shoes_data()
    while(True):
        menu_choice = input('''
        
What would you like to do?
1 - Display all shoes at all locations?
2 - Input a new shoe
3 - Search all locations for a specific shoe?
4 - Get total values for every shoe
5 - Re-Stock the lowest stocked shoe
6 - Put the highest stocked shoe on sale

0 - Quit
''')
        if menu_choice == "1":   view_all()
        elif menu_choice == "2":   capture_shoes()
        elif menu_choice == "3":
            search_keyword = input("Please input the code for the shoe you would like to search:\t")
            print(search_keyword)
            search_shoe(search_keyword)
        elif menu_choice == "4":   value_per_item()
        elif menu_choice == "5":   re_stock()
        elif menu_choice == "6":   highest_qty()
        elif menu_choice == "0":   
            print("Goodbye")
            time.sleep(1)
            break
            
menu()