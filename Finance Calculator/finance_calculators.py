#Imports math library
import math

#Initial instructions and information
print("Choose either \"Investments\" or \"Bonds\" \n  ")
print("Investments \t - to calculate the amount of interest you'll earn on interest")
print("Bonds\t \t - to calculate the amount you'll have to pay on a home load ")

#Gets user input. Converts to lower case
temp_choice = input("Enter choice now: ")
temp_choice = temp_choice.lower()   #Converts input to lower case
choice = temp_choice[0]             #<-- Takes the first letter of the choice. This is what we will be using for if statement.
                                    # The reasons for this, is even if the user spells Bonds or investments incorrect, 
                                    # it will still only be based off the first character. So if they type in investmints, it will
                                    # still use the i character, instead of the whole word. Meaning the if statement will still run
                                    # for investments

if (choice == "i"):

    #Gets user inputs. 
    print("\n\n\n\n\n----------------------------------------------------------------------------------")
    print("We need some more details from you.")
    deposit_total = int(input("How much will you be depositing: "))                               # We need this number to be an int
    interest_rate = input("How much interest will there be on your investment per year: ")     # We need this to stay as a string.
    years = int(input("How many years will you be planning on investing for: "))                  # We need this number to be an int

    #Gets interest varaible type. Convert to lower case. Also assists with some information
    print("\n\nSimple interest is based on the original deposit amount.")
    print("Compound interest is based on the accumulated amount acquired every month.")
    interest = input("Simple or Compound interest?: ")                                          
    interest = interest.lower()                                                                 # Converts to lower case. I could probably do this in the 
                                                                                                # same line as input, but its more readable like this
   
    interest = interest[0] #<-- Takes the first letter of the choice. This is what we will be using for if statement.
                            # The reasons for this, is even if the user spells Simple or Compound incorrect, 
                            # it will still only be based off the first character. So if they type in Componde, it will
                            # still use the c character, instead of the whole word. Meaning the if statement will still run
                            # for Compound

    if (interest_rate[-1] == "%") :                                  # Start of if statement. Checks if last char is %
        interest_rate = int(interest_rate.replace("%" , ""))      # If so, replace the last character with nothing. 
                                                                        # Also convert to int
    else :
        interest_rate = int(interest_rate)                        # Else just convert it to int
    interest_rate = interest_rate / 100                           # Changes interest rate (7%) to a number we can use (0.07)

    #Does the calculation for simple interest
    if (interest == "s"):                                          #If interest type is "simple"                    
        total = round(deposit_total*(1+interest_rate*years), 2)      # Does the calculation "A =P*(1+r*t)" with our given values
        print("\n\n\n----------------------------------------------------------------------------------")
        print("\nYour investment will total at R" + str(total))         # Prints total
        print("\n----------------------------------------------------------------------------------")

    #Does the calculation for compound interest
    elif (interest == "c"):                                                  #If interest type is "simple"      
        total = round(deposit_total * math.pow((1+ interest_rate), years) , 2)   # Does the calculation "P* math.pow((1+r),t)" with our given values
        print("\n\n\n----------------------------------------------------------------------------------")
        print("\nYour investment will total at R" + str(total))                     # Prints total
        print("\n----------------------------------------------------------------------------------")

    #Fault catching. Will catch anything that isnt an "s" or a "c"
    else:
        print("Something went wrong. Please try again")     # Lets user know there is a fault. 
                                                            # This could be drastically improved with a try catch statement

#if your choice was bonds
elif (choice == "b"):           #If your choice was Bonds, this runs. Again using only the first letter, to counter spelling errors
    #Gets user inputs
    print("\n\n\n----------------------------------------------------------------------------------")
    print("We need a few more details from you")
    house_value = int(input("Please input the value of the house : "))                          # We need this number as int
    interest_rate = input("Please input the annuel interest rate on the house : ")              # We need this number as string
    term = int(input("Please input the length of time you want to pay the bond (months) : "))   # We need this number as int

    if (interest_rate[-1] == "%") :                             # Start of if statement. Checks if last char is %
        interest_rate = int(interest_rate.replace("%" , ""))    # If so, replace the last character with nothing. 
                                                                # Also convert to int
    else :
        interest_rate = int(interest_rate)                      # Else just convert it to int
    interest_rate = interest_rate / 100                         # Changes interest rate (7%) to a number we can use (0.07)


    # Does the calculation. I have used this formula """ x = (r/12) * (1/(1-(1+r/12)**(-m)))*P """ To do the maths, rather then the one given
    # I was having issues with the one given, as I was struggling to get it to translate correctly into python.
    # This formula was found online. I do not take credit for the formula. Translating it into my code was done by me. The code is mine    

    x = (interest_rate/12) * (1/(1-(1+interest_rate/12)**(-term)))*house_value  # Does the maths with the formula
    total_per_month = round(x, 2)                                               # Rounds the number down to 2 decimal places
    print("\n\n\n----------------------------------------------------------------------------------")
    print("Your monthly payments will be R" + str(total_per_month))             # Final print
    print("----------------------------------------------------------------------------------")

#Fault catching. Will catch anything that isnt an "i" or a "b"
else:                                     
    print("Something went wrong. Please try again") # Lets user know there is a fault. 
                                                    # This could be drastically improved with a try catch statement


# Nearly got to 100 lines
