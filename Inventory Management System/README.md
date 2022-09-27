# **Inventory Management System**
### **Store inventory managerment program**

### **Instructions**

We were instructed to code in python a program that multiple stores could use to manage and update inventories

### **Method**

#### 1
Firstly, we created the Shoe object. This shoe has the following attributes:
    
    Country: Country where shoe is located
    Code: A unique code for that shoe
    Product: What the shoe is
    Cost: How much the shoe costs
    Quantity: How many of that shoe is at that store
    Value: The total value of the shoes, which is quantity x cost
    
Along with that object, there were the following methods for that object

    get_cost: Returns the cost of that shoe
    get_quantity: Gets total quantity of that shoe
    __STR__: Displays that shoe
    
    
#### 2
Following that, we created methods to do the following:

    read_shoes_data: Reads inventory, and updates a list
    capture_shoes: A method to capture information for a new shoe
    view_all: A method to view all shoes
    re_stock: A method to increase the stock of the lowest stocked shoe
    min_max: Gets the highest/lowest stock counts. Returns a list
    search_shoe: Allows to search the invetory for a specific code
    value_per_item: Returns a string, with information of the values of the shoe
    highest_qty: Gets the highest stocked shoe, and puts a 10% sale on it
    menu: Creates a displayed menu for the user to use
    
#### 3
The user will have access to the following menu

     
    What would you like to do?
    1 - Display all shoes at all locations?
    2 - Input a new shoe
    3 - Search all locations for a specific shoe?
    4 - Get total values for every shoe
    5 - Re-Stock the lowest stocked shoe
    6 - Put the highest stocked shoe on sale
    0 - Quit
    
Where they can access the required features they want to use
    
  
